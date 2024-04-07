from django.contrib import admin
from django.urls import path
from main import views


app_name = "main"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("pizza-details", views.test_pizza_ajax, name="pizza-details"),
    path("product/<slug:product_slug>/", views.product, name="product"),
    path("about", views.about, name="about"),
    path('your-endpoint-url/', views.your_view_name, name='your_view_name'),
    path('api/', views.product, name='api')
]
