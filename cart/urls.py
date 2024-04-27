from django.contrib import admin
from django.urls import path
from cart import views


app_name = 'cart'

urlpatterns = [
    path('cart_add/', views.cart_add, name='cart_add'),
    path('cart_change/', views.cart_change, name='cart_change'),
    path('cart_remove/', views.cart_remove, name='cart_remove'),
    path('', views.cart, name='cart_view'),
]