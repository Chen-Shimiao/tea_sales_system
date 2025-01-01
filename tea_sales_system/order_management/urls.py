from django.urls import path
from . import views

urlpatterns = [
    path('order_create/', views.order_create, name='order_create'),
    path('order_list/', views.order_list, name='order_list'),
    path('<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/direct/<int:product_id>/', views.direct_order, name='direct_order'),
    path('ship/<int:order_id>/', views.order_ship, name='order_ship'),
    path('pay/<int:order_id>/', views.order_pay, name='order_pay'),
    path('receive/<int:order_id>/', views.order_receive, name='order_receive'),
    path('review/<int:order_id>/', views.order_review, name='order_review'),
    path('cancel/<int:order_id>/', views.order_cancel, name='order_cancel'),
    path('orders/status/<str:status>/', views.order_list_by_status, name='order_list_by_status'),
    path('orders/<int:order_id>/products/<int:product_id>/review/', views.create_review, name='create_review'),
]
