from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('product_management.urls')),
    path('', include('sales_system.urls')),
    path('', include('user_management.urls')),
    path('', include('order_management.urls')),
    path('admin/', admin.site.urls),
]