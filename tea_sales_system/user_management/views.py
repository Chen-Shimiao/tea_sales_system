import json
import os

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from .backends import CustomAuthBackend
from .forms import UserForm, AddressForm, UserForm
from .models import User, Address


def user_list(request):
    users = User.objects.all()
    paginator = Paginator(users, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'users/user_list.html', {'page_obj': page_obj})


# 用户注册视图
def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')
        form = UserForm(request.POST)
        # 校验密码是否匹配
        if password1 != password2:
            messages.error(request, "密码不匹配，请重新输入")
            return render(request, 'users/register.html')

        # 验证密码强度
        try:
            validate_password(password1)
        except ValidationError as e:
            messages.error(request, e)  # 显示密码校验错误信息
            return render(request, 'users/register.html')

        # 创建新用户
        form.save()
        messages.success(request, f"{username}注册成功，请登录")
        return redirect('user_login')
# 如果不是POST请求，返回注册页面
    return render(request, 'users/register.html')  # 返回render

def user_login(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            # 手动检查密码是否为明文
            user = User.objects.filter(username=username).first()
            if user and check_password(password, user.password):
                user.password = make_password(password)
                user.save()
                user = authenticate(request, username=username, password=password)
        if user is not None:
            user.backend = 'user_management.backends.CustomAuthBackend'
            login(request, user)
            return redirect('product_sales_list')  # 登录成功后重定向到主页
        else:
            messages.error(request, '用户名或密码不正确')
    return render(request, 'users/login.html')

def user_logout(request):
    if request.method == 'GET':
        logout(request)
        return HttpResponseRedirect('/user_login/')

# 用户创建视图
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully.")
            return redirect(reverse('user_list'))
    else:
        form = UserForm()
    return render(request, 'users/user_create.html', {'form': form})

# 用户编辑视图
def user_edit(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully.")
            return redirect(reverse('user_list'))
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_edit.html', {'form': form, 'user': user})


# 用户删除视图
def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, "User deleted successfully.")
    return redirect(reverse('user_list'))


def address_list(request):
    addresses = Address.objects.filter(user=request.user)
    return render(request, 'addresses/address_list.html', {'addresses': addresses})


def address_add(request):
    json_file_path = os.path.join('user_management', 'static', 'cities.json')  # 替换为你的路径
    with open(json_file_path, 'r', encoding='utf-8') as f:
        cities_data = json.load(f)
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('address_list')
    else:
        form = AddressForm()
    return render(request, 'addresses/address_form.html', {'form': form, 'cities_data': cities_data})
    #return render(request, 'addresses/address_form.html', {'form': form})


def address_edit(request, address_id):
    json_file_path = os.path.join('user_management', 'static', 'cities.json')  # 替换为你的路径
    with open(json_file_path, 'r', encoding='utf-8') as f:
        cities_data = json.load(f)
    address = get_object_or_404(Address, id=address_id, user=request.user)
    selected_province = address.province
    selected_city = address.city
    selected_district = address.district
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('address_list')
    else:
        form = AddressForm(instance=address)
    return render(request, 'addresses/address_form.html', {'form': form, 'cities_data': cities_data,
                                                           "selected_province": selected_province,
        "selected_city": selected_city,
        "selected_district": selected_district,})


def address_delete(request, address_id):
    address = get_object_or_404(Address, id=address_id, user=request.user)
    if request.method == 'POST':
        address.delete()
        return redirect('address_list')
    return render(request, 'addresses/address_confirm_delete.html', {'address': address})


def personal_details(request):
    username=request.user.username
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully.")
    else:
        form = UserForm(instance=user)
    return render(request, 'users/personal_details.html', {'form': form, 'user': user})
