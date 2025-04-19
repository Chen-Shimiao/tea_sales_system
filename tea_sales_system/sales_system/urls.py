from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('cart_add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart_update/<int:product_id>/', views.cart_add, name='cart_update'),
    path('cart_remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('product_sales_list/', views.product_sales_list, name='product_sales_list'),
    path('sales_analysis/', views.sales_analysis, name='sales_analysis'),
    path('announcements/', views.announcement_list, name='announcement_list'),
    path('announcements/add/', views.announcement_create, name='announcement_add'),
    path('announcements/<int:pk>/edit/', views.announcement_update, name='announcement_edit'),
    path('announcements/<int:pk>/delete/', views.announcement_delete, name='announcement_delete'),
    path('system_index/', views.index, name='index'),
    path('products_by_category/', views.products_by_category, name='products_by_category'),
    path('category/<int:category_id>/products/', views.products_in_category, name='category_products'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)