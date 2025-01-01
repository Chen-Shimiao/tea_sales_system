from django import template
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ReviewForm
from .models import Order, Evaluation
from user_management.models import Address

from sales_system.views import calculate_cart
from product_management.models import Product



def apply_promotions(product, promotions, quantity):
    """
    根据商品和促销活动计算最终价格。
    """
    original_price = product.sales_price * quantity
    discount = 0

    for promo in promotions:
        # 满减活动
        if promo.promotion_type == 'full_reduce':
            if original_price >= promo.full_price:
                discount += promo.reduction_price

        # 满赠活动
        elif promo.promotion_type == 'buy_gift':
            if quantity >= promo.buy_quantity:
                free_items = promo.gift_quantity // promo.condition
                discount += free_items * product.price

        # 打折活动
        elif promo.promotion_type == 'discount':
            discount += original_price *  (1-promo.discount)

    # 计算最终价格
    final_price = max(original_price - discount, 0)
    return final_price, discount

def order_create(request):
    from .models import OrderItem
    from .forms import OrderForm
    from user_management.models import Address
    from user_management.forms import AddressForm
    from sales_system.utils import Cart
    print(request.POST)
    if request.method == 'POST':
        print(1)
        order_form = OrderForm(request.POST, user=request.user)
        address_form = AddressForm(request.POST)
        if 'select_address' in request.POST:
            print(2)
            address_id = request.POST.get('address')
            address = Address.objects.get(id=address_id, user=request.user)
            cart = Cart(request)
            if not cart.cart:
                return redirect('cart_detail')  # 如果购物车为空，返回购物车页面
            cart_data=calculate_cart(request)
            # 计算总价和优惠
            total_price = cart.get_total_price()
            discounted_total=cart_data['final_price']
            discount = cart_data['total_discount']

            # 创建订单
            order = Order.objects.create(
                user=request.user,
                address=address,
                total_price=total_price,
                discount=discount,
                final_price=discounted_total,
            )
            order.save()
            print(3)
            # 创建订单项
            for item in cart:
                product = item['product']

                # 检查库存（如果需要）
                if product.stock < item['quantity']:
                    return render(request, 'cart_detail.html', {
                        'cart': cart,
                        'error': f"商品 {product.name} 库存不足！",
                    })

                # 减库存
                product.stock -= item['quantity']
                product.save()

                # 创建订单项
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    price=item['price'],
                    quantity=item['quantity']
                )
            print(98)
            # 清空购物车
            cart.clear()
            return redirect('order_list')
        elif 'add_address' in request.POST:
            if address_form.is_valid():
                address = address_form.save(commit=False)
                address.user = request.user
                address.save()
                return redirect('order_create')  # 地址保存后刷新下单页面
    else:
        order_form = OrderForm(user=request.user)
        address_form = AddressForm()
    return render(request, 'order_create.html', {
        'order_form': order_form,
        'address_form': address_form, })


def direct_order(request, product_id):
    from order_management.forms import OrderForm, DirectOrderForm
    from order_management.models import Order, OrderItem
    from product_management.models import Product
    product = get_object_or_404(Product, id=product_id)
    promotions = product.promotions.all()  # 获取商品关联的促销活动
    quantity = int(request.POST.get('quantity', 1))  # 用户选择的数量，默认为1

    # 计算原价
    total_price = product.sales_price * quantity

    # 计算促销价格
    final_price, discount = apply_promotions(product, promotions, quantity)

    if request.method == 'POST':
        # 获取用户选择的地址
        address_id = request.POST.get('address')
        address = Address.objects.get(id=address_id, user=request.user)

        # 创建订单
        order = Order.objects.create(
            user=request.user,
            address=address,
            total_price=total_price,
            discount=discount,
            final_price=final_price,
        )

        # 创建订单项
        OrderItem.objects.create(
            order=order,
            product=product,
            price=product.sales_price,
            quantity=quantity,
        )

        # 更新库存
        product.stock -= quantity
        product.save()

        return redirect('order_detail', order_id=order.id)

    addresses = Address.objects.filter(user=request.user)
    return render(request, 'direct_order.html', {
        'product': product,
        'quantity': quantity,
        'total_price': total_price,
        'final_price': final_price,
        'discount': discount,
        'addresses': addresses,
    })


def order_list(request):
    from order_management.models import Order
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_list.html', {'orders': orders})


def order_detail(request, order_id):
    from order_management.models import Order
    order = get_object_or_404(Order, id=order_id, user=request.user)
    evaluations = {}

    # 检查订单中每个商品是否已被评价
    for item in order.items.all():
        evaluations[item.product.id] = Evaluation.objects.filter(
            order=order,
            product=item.product,
            user=request.user
        ).exists()

    context = {
        'order': order,
        'evaluations': evaluations,  # 商品评价状态
    }
    return render(request, 'order_detail.html', context)


def order_pay(request, order_id):
    from order_management.models import Order
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method', '')
        if not payment_method:
            return JsonResponse({'message': 'Payment method is required'}, status=400)
        if order.status == 'pending_payment':
            try:
                #if payment_method == 'alipay':
                    # service = AlipayService()
                # elif payment_method == 'wechat':
                #     service = WeChatPayService()
                # elif payment_method == 'paypal':
                #     service = PayPalService()
                # if payment_method == 'alipay':
                #     return JsonResponse({'message': '支付宝支付成功！'}, status=400)
                # elif payment_method == 'wechat':
                #     return JsonResponse({'message': '微信支付成功！'}, status=400)
                # elif payment_method == 'paypal':
                #     return JsonResponse({'message': '银行卡支付成功！'}, status=400)
                # else:
                #     return JsonResponse({'message': 'Unsupported payment method'}, status=400)
                order.status = 'pending_shipment'
                order.save()
                # return redirect(payment_url)
                # create_alipay_order(request)

            except Exception as e:
                return JsonResponse({'message': str(e)}, status=500)
    return redirect('order_list_by_status', status='pending_payment')

def order_cancel(request, order_id):
    from order_management.models import Order
    order = get_object_or_404(Order, id=order_id)
    order.status = 'cancelled'
    order.save()
    return redirect('order_list_by_status', status='pending_payment')


def order_ship(request, order_id):
    from order_management.models import Order
    order = get_object_or_404(Order, id=order_id)

    # 只有管理员可以标记订单为已发货
    if not request.user.is_staff:
        return HttpResponseForbidden("您没有权限。")

    if order.status == 'pending_shipment':
        order.status = 'pending_receipt'
        order.save()

    return redirect('order_list_by_status', status='pending_shipment')

def order_receive(request, order_id):
    from order_management.models import Order
    order = get_object_or_404(Order, id=order_id)

    if order.status == 'pending_receipt':
        order.status = 'pending_review'
        order.save()

    return redirect('order_list_by_status', status='pending_receipt')

def order_review(request, order_id):
    from order_management.models import Order
    order = get_object_or_404(Order, id=order_id)

    return redirect('order_detail', order_id=order_id)

def order_list_by_status(request, status):
    # 验证状态值是否合法
    # valid_statuses = ['pending_payment', 'pending_shipment', 'pending_receipt', 'pending_review', 'completed',
    #                   'canceled','all']
    # if status not in valid_statuses:
    #     # 如果状态不合法，可以返回一个错误页面或重定向到默认页面
    #     return render(request, 'orders/invalid_status.html')
    from order_management.models import Order
    # 根据状态值筛选订单
    if request.user.is_staff:
        # 管理员可以查看所有订单
        if status == 'all':
            orders = Order.objects.filter()
        else:
            orders = Order.objects.filter(status=status)
    else:
        # 普通用户只能查看自己的订单
        if status == 'all':
            orders = Order.objects.filter(user=request.user)
        else:
            orders = Order.objects.filter(status=status, user=request.user)
    context = {
        'orders': orders,
        'status': status,
        'is_staff':request.user.is_staff,
    }
    print(request.user.is_staff)
    return render(request, 'order_list.html', context)


def create_review(request, order_id, product_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    product = get_object_or_404(Product, id=product_id)

    # 检查用户是否已经评价过该商品
    if Evaluation.objects.filter(order=order, product=product, user=request.user).exists():
        messages.error(request, "您已经评价过该商品")
        return redirect('order_detail', order_id=order.id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.order = order
            review.product = product
            review.save()
            messages.success(request, "评价提交成功！")
            if order.status == 'pending_review':
                order.status = 'completed'
                order.save()
            return redirect('order_detail', order_id=order.id)
    else:
        form = ReviewForm()

    return render(request, 'create_review.html', {'form': form, 'order': order, 'product': product})