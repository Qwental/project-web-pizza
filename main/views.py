from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
import json
from main.models import Category, Products
from django.views.decorators.csrf import csrf_exempt


def index(request):
    """
    Контроллер, отвечающий за главную страницу с меню.
    """

    categories = Category.objects.all()

    context = {
        "categories": categories,
    }
    return render(request, "main/index.html", context=context)


"""def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    product_options = product.options
    if product_options != "":
        options_json = json.loads(product_options)
    else:
        options_json = None

    context = {
        "product": product,
        "options": options_json,
    }
    return render(request, "main/product.html", context=context)
    """


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
        # делаем из него обычный массив
        items = data.get("items", [])
        response_creator = []
        # для каждого продукта в корзине...
        for item in items:
            # получаем id и опции
            item_id = item.get("id")
            data_dict = item.get("data")

            # получаем продукт по id (де-факто его название и описание с картинкой)
            product = Products.objects.get(id=item_id)

            # махинации с ценами
            price = product.sell_price()

            if data_dict["size"] == "small":
                price += 0
            if data_dict["size"] == "medium":
                price += 100
            if data_dict["size"] == "large":
                price += 200
            if len(data_dict["toppings"]) == 0:
                price += 0
            if len(data_dict["toppings"]) == 1:
                price += 10
            if len(data_dict["toppings"]) == 2:
                price += 20
            if len(data_dict["toppings"]) == 3:
                price += 30

            # создаем мини-джэйсона для массива, который мы потом вернем
            responseCreatorElem = {
                "name": product.name,
                "price": price,
                "description": product.description,
            }
            response_creator.append(responseCreatorElem)

        return JsonResponse(response_creator, safe=False)
    

def product(request):
    if request.method == 'GET':
        product_id = request.GET.get('id')

        cur_product = Products.objects.get(id=product_id)
        context = {
            'name': cur_product.name,
            'price': cur_product.sell_price(),
            'options': cur_product.options,
        }

        return JsonResponse(context, safe=False, json_dumps_params={'ensure_ascii': False}, content_type='application/json; charset=utf-8')
    

