from django.urls import path
from . import views

urlpatterns = [
    path('product_management/', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_add, name='product_add'),
    path('products/edit/<int:product_id>/', views.product_edit, name='product_edit'),
    path('products/delete/<int:product_id>/', views.product_delete, name='product_delete'),
    path('products/update_stock/<int:product_id>/', views.update_stock, name='update_stock'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/update/<int:category_id>/', views.category_update, name='category_update'),
    path('categories/delete/<int:category_id>/', views.category_delete, name='category_delete'),
    path('products/update_promotion/<int:product_id>/',views.update_promotion,name='update_promotion'),
]