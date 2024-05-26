from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('create-order/', views.create_order, name='create_order'),
    path('create-order-pickup/', views.create_order_pickup, name='create_order_pickup'),
    path('success/', views.success, name='success'),
    path('delivery_or_pickup/', views.delivery_or_pickup, name='delivery_or_pickup'),
]