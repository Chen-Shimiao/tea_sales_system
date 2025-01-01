from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Promotion
from .forms import ProductForm, CategoryForm


def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category created successfully.")
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'categories/category_form.html', {'form': form})

def category_update(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category updated successfully.")
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/category_form.html', {'form': form})

def category_delete(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        messages.success(request, "Category deleted successfully.")
        return redirect('category_list')
    return render(request, 'categories/category_confirm_delete.html', {'category': category})

def update_promotion(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        promotion_id = request.POST.get('promotion')
        if promotion_id:
            promotion = get_object_or_404(Promotion, id=promotion_id)
            product.promotions.add(promotion)
            product.save()
            return redirect('product_list')  # 重定向到商品管理页面

    return HttpResponse("请求方法错误", status=400)

def product_list(request):
    products = Product.objects.prefetch_related('promotion').all()
    for p in products:
        print(p.promotion)
    return render(request, 'products/product_list.html', {'products': products})

def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            print(form.errors)
            print("FILES data:", request.FILES)
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})

def product_edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form})

def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})

def update_stock(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        quantity = int(request.POST.get('quantity'))
        if action == 'increase':
            product.increase_stock(quantity)
        elif action == 'reduce':
            product.reduce_stock(quantity)
        return redirect('product_list')
    return render(request, 'products/update_stock.html', {'product': product})
