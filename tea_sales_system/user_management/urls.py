from django.urls import path
from . import views

urlpatterns = [
    path('user_management/user_list/', views.user_list, name='user_list'),
    path('user_management/user_create/', views.user_create, name='user_create'),
    path('user_management/user_edit/<int:user_id>/', views.user_edit, name='user_edit'),
    path('user_management/personal_details/', views.personal_details, name='personal_details'),
    path('user_management/user_delete/<int:user_id>/', views.user_delete, name='user_delete'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('user_register/', views.user_register, name='user_register'),
    path('addresses/', views.address_list, name='address_list'),
    path('addresses/add/', views.address_add, name='address_add'),
    path('addresses/edit/<int:address_id>/', views.address_edit, name='address_edit'),
    path('addresses/delete/<int:address_id>/', views.address_delete, name='address_delete'),
]