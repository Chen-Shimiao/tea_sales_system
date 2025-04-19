import json

import pandas as pd
from django.db.models import F, Case, When, Value, CharField, Sum
from django.db.models.functions import TruncDate, TruncMonth
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from product_management.models import Product,Promotion,Category, Origin
from order_management.models import Order, OrderItem
from alipay import AliPay

from tea_sales_system import settings
from sales_system.models import Announcement

from sales_system.forms import AnnouncementForm


def base(request):
    announcements = Announcement.objects.filter(is_active=True).order_by('-created_at')[:5]  # 获取最新的5个公告

    return render(request, 'home.html',
                  {'announcements': announcements})

def product_sales_list(request):
    # 查询所有商品及其促销信息
    category_id = request.GET.get('category')
    origin_id = request.GET.get('origin')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    # 获取排序参数，默认为按创建时间倒序
    sort_by = request.GET.get('sort', '-id')

    # 排序字段映射，防止用户传入非法字段
    valid_sort_options = {
        'price_asc': 'sales_price',  # 价格升序
        'price_desc': '-sales_price',  # 价格降序
        'name_asc': 'name',  # 名称升序
        'name_desc': '-name',  # 名称降序
        'latest': '-id',  # 最新商品
    }
    sort_field = valid_sort_options.get(sort_by, '-id')  # 默认排序

    # 构造查询
    products = Product.objects.prefetch_related('promotion').all()
    if category_id:
        products = products.filter(category_id=category_id)
    if origin_id:
        products = products.filter(origin_id=origin_id)
    if min_price:
        products = products.filter(sales_price__gte=min_price)
    if max_price:
        products = products.filter(sales_price__lte=max_price)

    products=products.order_by(sort_field)
    # 获取所有分类和品牌用于展示
    categories = Category.objects.all()
    origins = Origin.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'origins': origins,
        'sort_by': sort_by,
    }

    return render(request, "product_sales_list.html", context)

def index(request):
    # 查询所有商品及其促销信息
    category_id = request.GET.get('category')
    origin_id = request.GET.get('origin')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    # 获取排序参数，默认为按创建时间倒序
    sort_by = request.GET.get('sort', '-id')

    # 排序字段映射，防止用户传入非法字段
    valid_sort_options = {
        'price_asc': 'sales_price',  # 价格升序
        'price_desc': '-sales_price',  # 价格降序
        'name_asc': 'name',  # 名称升序
        'name_desc': '-name',  # 名称降序
        'latest': '-id',  # 最新商品
    }
    sort_field = valid_sort_options.get(sort_by, '-id')  # 默认排序

    # 构造查询
    products = Product.objects.prefetch_related('promotion').all()
    if category_id:
        products = products.filter(category_id=category_id)
    if origin_id:
        products = products.filter(origin_id=origin_id)
    if min_price:
        products = products.filter(sales_price__gte=min_price)
    if max_price:
        products = products.filter(sales_price__lte=max_price)

    products=products.order_by(sort_field)
    # 获取所有分类和品牌用于展示
    categories = Category.objects.all()
    origins = Origin.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'origins': origins,
        'sort_by': sort_by,
    }

    return render(request, "index.html", context)

def cart_add(request, product_id):
    from .utils import Cart, recommend_products
    from product_management.models import Product
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product=product, quantity=quantity, update_quantity=True)
    return redirect('cart_detail')


def cart_remove(request, product_id):
    from .utils import Cart, recommend_products
    from product_management.models import Product
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_update(request, product_id):
    from .utils import Cart
    tea = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))  # 获取更新的数量
    cart = Cart(request)
    cart.add(tea, quantity, update_quantity=True)
    return redirect('cart_detail')

def calculate_product_promotion(sales_price, quantity, promotions):
    """
    计算单个商品促销后的价格
    :param product: 商品对象
    :param quantity: 商品数量
    :param promotions: 促销活动列表
    :return: 促销后的总价
    """
    total_price = sales_price * quantity

    for promo_id in promotions:
        promotion = get_object_or_404(Promotion, id=promo_id)

        if promotion.promotion_type == 'discount':
            total_price *= promotion.discount

        elif promotion.promotion_type == 'buy_gift' and quantity > promotion.buy_quantity:
            free_items = quantity // promotion.buy_quantity
            total_price -= free_items * sales_price

    return max(total_price, 0)

def calculate_global_promotion(cart_total_full_reduce):
    """
    计算全局促销活动的优惠金额
    :param cart_total: 购物车总金额（商品促销后的总价）
    :param global_promotions: 全局促销活动列表
    :return: 总优惠金额
    """
    discount = 0

    promotion = get_object_or_404(Promotion, promotion_type='full_reduction')
    if cart_total_full_reduce >= promotion.full_price:
        discount += promotion.reduction_price

    return discount

def calculate_cart(request):
    """
    计算购物车促销后的总价和优惠金额
    """
    from .utils import Cart
    cart = Cart(request)
    print(cart)
    product_details = []
    cart_total = 0
    total_discount = 0
    cart_total_full_reduce=0
    # 逐个商品计算
    for item in cart:
        price=item['price']
        quantity = item['quantity']
        promotions = item['promotions']
        print(item)
        # 商品促销计算
        product_price = calculate_product_promotion(price, quantity, promotions)
        original_price = price * quantity
        discount = original_price - product_price
        # 累计促销后总价和商品详情
        for promo_id in promotions:
            promotion = get_object_or_404(Promotion, id=promo_id)
            print(promotion.promotion_type)
            if promotion.promotion_type == 'full_reduction':
                cart_total_full_reduce += product_price
        cart_total+=product_price
        total_discount += discount
        print(total_discount)
        product_details.append({
            'quantity': quantity,
            'original_price': original_price,
            'discounted_price': product_price,
            'discount': discount
        })

    # 全局促销计算
    global_discount = calculate_global_promotion(cart_total_full_reduce)
    total_discount += global_discount
    final_price = cart_total - global_discount

    return {
        'cart_total': cart_total,
        'global_discount': global_discount,
        'total_discount': total_discount,
        'final_price': final_price
    }

def cart_detail(request):
    from .utils import Cart
    cart = Cart(request)
    cart_data=calculate_cart(request)
    return render(request, 'cart_detail.html', {
        'cart': cart,
        'total_price': cart_data['cart_total'],
        'discounted_total': cart_data['total_discount'],
        'final_price': cart_data['final_price'],
    })


def recommend_view(request, user_id):
    from .utils import recommend_products
    recommended_products = recommend_products(user_id)
    return render(request, 'recommendations.html', {'products': recommended_products})


def sales_analysis(request):
    # 查询订单并提取日期
    orders = Order.objects.annotate(created_date=TruncDate('created_at'),status_display=Case(
            When(status='pending_payment', then=Value('待付款')),
            When(status='pending_shipment', then=Value('待发货')),
            When(status='pending_receipt', then=Value('待收货')),
            When(status='pending_review', then=Value('待评价')),
            When(status='completed', then=Value('已完成')),
            When(status='cancelled', then=Value('已取消')),
            default=Value('未知状态'),
            output_field=CharField(),
        )).values('id', 'created_date','final_price','status_display')
    monthly_sales = (
        Order.objects.annotate(month=TruncMonth('created_at'))
        .values('month')
        .annotate(total_sales=Sum('final_price'))
        .order_by('month')
    )
    # 查询订单项，并获取产品的分类和产地信息
    order_items = OrderItem.objects.select_related('product').values(
        'order_id', 'product__name', 'product__category__name', 'product__origin__name', 'quantity', 'price'
    )
    for order in orders:
        # 将 UTC 时间转换为本地时间
        order['created_date'] = order['created_date'].strftime('%Y-%m-%d')
        order['final_price'] = float(order['final_price'])
    # 转换为 Pandas 数据框
    orders_df = pd.DataFrame(list(orders))
    order_items_df = pd.DataFrame(list(order_items))

    if orders_df.empty or order_items_df.empty:
        return render(request, 'sales_analysis.html', {'error': '没有销售数据'})
    order_status_counts = orders_df['status_display'].value_counts().to_dict()
    # 合并订单和订单项
    merged_df = pd.merge(order_items_df, orders_df, left_on='order_id', right_on='id')

    # 计算每个订单项的销售总额
    merged_df['item_total'] = merged_df['quantity'] * merged_df['price']

    # 统计每日销售额
    daily_sales = merged_df.groupby('created_date')['final_price'].sum().to_dict()

    # 统计热销商品
    top_products = merged_df.groupby('product__name')['quantity'].sum().sort_values(ascending=False).head(
        5).to_dict()

    # 统计各分类的销量（用于饼状图）
    category_sales = merged_df.groupby('product__category__name')['quantity'].sum().to_dict()

    # 统计各产地的销量（用于饼状图）
    origin_sales = merged_df.groupby('product__origin__name')['quantity'].sum().to_dict()

    monthly_sales_data = {item['month'].strftime('%Y-%m'): float(item['total_sales']) for item in monthly_sales}
    # 传递数据到模板
    context = {
        'daily_sales': daily_sales,
        'top_products': top_products,
        'category_sales': category_sales,  # 商品分类销量数据
        'origin_sales': origin_sales,  # 产地销量数据
        'order_status_counts': order_status_counts,
        'monthly_sales': json.dumps(monthly_sales_data),
    }
    return render(request, 'sales_analysis.html', context)


def create_alipay_order(request):
    alipay = AliPay(
        appid=settings.ALIPAY['appid'],
        app_notify_url=settings.ALIPAY['app_notify_url'],
        app_private_key_path=settings.ALIPAY['app_private_key_path'],
        alipay_public_key_path=settings.ALIPAY['alipay_public_key_path'],
        sign_type=settings.ALIPAY['sign_type'],
    )

    order_string = alipay.api_alipay_trade_app_pay(
        subject="Test Product",
        out_trade_no="order123456",
        total_amount=100.00,
        product_code="QUICK_MSECURITY_PAY",
    )

    return JsonResponse({'order_string': order_string})


def alipay_notify(request):
    alipay = AliPay(
        appid=settings.ALIPAY['appid'],
        app_notify_url=settings.ALIPAY['app_notify_url'],
        app_private_key_path=settings.ALIPAY['app_private_key_path'],
        alipay_public_key_path=settings.ALIPAY['alipay_public_key_path'],
        sign_type=settings.ALIPAY['sign_type'],
    )

    # 获取支付回调数据
    data = request.POST

    # 验证签名
    if alipay.verify(data):
        # 支付成功的处理逻辑
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'failure'})

def announcement_list(request):
    announcements = Announcement.objects.order_by('-created_at')
    return render(request, 'announcements/list.html', {'announcements': announcements})

def announcement_create(request):
    form = AnnouncementForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('announcement_list')
    return render(request, 'announcements/form.html', {'form': form})

def announcement_update(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    form = AnnouncementForm(request.POST or None, instance=announcement)
    if form.is_valid():
        form.save()
        return redirect('announcement_list')
    return render(request, 'announcements/form.html', {'form': form})

def announcement_delete(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        announcement.delete()
        return redirect('announcement_list')
    return render(request, 'announcements/confirm_delete.html', {'announcement': announcement})

def products_by_category(request):
    parent_categories = Category.objects.filter(parent__isnull=True)

    # 构造一个字典：{ 父分类: 子分类商品列表 }
    category_products = {}

    for parent in parent_categories:
        # 获取子分类们
        subcategories = parent.subcategories.all()

        # 获取这些子分类下的所有商品
        products = Product.objects.filter(category__in=subcategories).select_related('category')

        category_products[parent] = products

    return render(request, 'products_by_category.html', {
        'category_products': category_products
    })

def products_in_category(request, category_id):
    parent_category = get_object_or_404(Category, id=category_id)
    # 获取所有子分类
    subcategories = parent_category.subcategories.all()
    # 获取所有子分类的商品
    products = Product.objects.filter(category__in=subcategories)

    return render(request, 'products_in_category.html', {
        'parent_category': parent_category,
        'products': products
    })