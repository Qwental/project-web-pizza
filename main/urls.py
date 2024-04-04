from django.contrib import admin
from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('pizza-details', views.test_pizza_ajax, name='pizza-details'),
]
