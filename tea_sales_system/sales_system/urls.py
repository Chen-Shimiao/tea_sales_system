from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('sales_system/', views.base, name='base'),
    path('cart_add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart_update/<int:product_id>/', views.cart_add, name='cart_update'),
    path('cart_remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('product_sales_list/', views.product_sales_list, name='product_sales_list'),
    path('sales_analysis/', views.sales_analysis, name='sales_analysis'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)