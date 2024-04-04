from unicodedata import category
from django.shortcuts import render
from django.http import JsonResponse

from main.models import Category, Products


def index(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'main/index.html', context=context)


def test_pizza_ajax(request):
    product_id = request.GET.get('id')
    
    try:
        product = Products.objects.get(id=product_id)
        product_data = {
            'name': product.name,
            'price': product.sell_price()  # Используем метод sell_price для подсчета цены с учетом скидки
        }
    except Products.DoesNotExist:
        product_data = {}

    return JsonResponse(product_data)