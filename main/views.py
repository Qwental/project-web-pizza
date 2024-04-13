from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
import json
from main.models import Category, Products, SpecialOffers
from django.views.decorators.csrf import csrf_exempt


def index(request):
    """
    Контроллер, отвечающий за главную страницу с меню.
    """

    categories = Category.objects.all()
    special_offers = SpecialOffers.objects.all()

    context = {
        "categories": categories,
        "special_offers": special_offers,
    }
    return render(request, "main/index.html", context=context)



def about(request):
    pass


def test_pizza_ajax(request):
    product_id = request.GET.get("id")

    try:
        product = Products.objects.get(id=product_id)
        product_data = {
            "name": product.name,
            "price": product.sell_price(),  # Используем метод sell_price для подсчета цены с учетом скидки
        }
    except Products.DoesNotExist:
        product_data = {}

    return JsonResponse(product_data)


def your_view_name(request) -> JsonResponse:
    """Калькулирует цену в корзине согласно добавленным опциям

    Args:
        request (json): полученные с фронтенда id товара и его опции

    Returns:
        json: название, картинка, описание и итоговая цена
    """
    if request.method == "POST":
        # получаем джэйсона из rest-запроса
        data = json.loads(request.body)
        print(data)
        return JsonResponse({'message': 'Пиривет', "data": data}, safe=False)
    

def product(request):
    """
    Возвращает Json с характеристиками товара из бд
    """
    if request.method == 'GET':
        product_id = request.GET.get('id')

        cur_product = Products.objects.get(id=product_id)
        context = {
            'name': cur_product.name,
            'price': cur_product.sell_price(),
            'img': str(cur_product.image.url),
            'options': cur_product.options,
        }

        return JsonResponse(context, safe=False, json_dumps_params={'ensure_ascii': False}, content_type='application/json; charset=utf-8')
    

