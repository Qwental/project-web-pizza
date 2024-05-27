import json

from django.http import HttpRequest
from django.http import JsonResponse
from django.shortcuts import render
from django.templatetags.static import static

from main.models import Category, Products, SpecialOffers


def index(request):
    """
    Контроллер, отвечающий за главную страницу с меню.
    """

    categories = Category.objects.all()
    special_offers = SpecialOffers.objects.all()
    count_offers = range(special_offers.count())

    context = {
        "categories": categories,
        "special_offers": special_offers,
        "count_offers": count_offers,
    }
    return render(request, "main/index.html", context=context)



def about(request: HttpRequest):
    """
    Контроллер, отвечающий за страницу "о нас" (about_page.html),
    та в свою очередь подгружает стили
    из папки styles_for_about_page
    """
    context = {

    }
    return render(request, 'main/about_page.html', context=context)

def contacts(request: HttpRequest):
    """
    Контроллер, отвечающий за страницу "Контакты" (contacts.html),
    та в свою очередь подгружает стили
    из папки styles_for_contacts_page
    """
    context = {

    }
    return render(request, 'main/contacts.html', context=context)


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
    context = {}
    if request.method == 'GET':
        product_id = request.GET.get('id')

        cur_product = Products.objects.get(id=product_id)
        context = {
            'name': cur_product.name,
            'price': cur_product.sell_price(),
            'options': cur_product.options,
            'img':  static('img/600x400.png')
        }
    
        if cur_product.image:
            context['img'] = str(cur_product.image.url)

    return JsonResponse(context, safe=False, json_dumps_params={'ensure_ascii': False}, content_type='application/json; charset=utf-8')
    

def not_found_page(request, exception):
    """
    Пользовательское представление для обработки ошибок 404.
    """
    return render(request, 'main/404.html', status=404)