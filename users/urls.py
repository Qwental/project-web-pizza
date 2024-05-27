from django.contrib import admin
from django.urls import path
from users import views


app_name = "users"

urlpatterns = [
    path('lost_pass/', views.lost_pass, name='lost_pass'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
]
