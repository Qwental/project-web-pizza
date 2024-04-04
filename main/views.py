from django.shortcuts import render
from django.http import JsonResponse
import json
from main.models import Category, Products


def index(request):
    """
    Контроллер, отвечающий за главную страницу с меню.
    """

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'main/index.html', context=context)



def product(request, product_slug):
    """
    Контроллер, отвечающий за страницу товара.
    """

    product = Products.objects.get(slug=product_slug)

    product_options = product.options
    if product_options != '':
        options_json = json.loads(product_options)
    else:
        options_json = None

    context = {
        'product':  product,
        'options': options_json,
    }
    return render(request, 'main/product.html', context=context)


def about(request):
    pass



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