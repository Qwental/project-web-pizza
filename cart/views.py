import json
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

from cart.models import Cart
from main.models import Products

# TODO: ВАНЯ ПОПРАВЬ __message, а то там всегда "Ошибка добавления товара в корзину" и не отображается успешный-попап
def cart_add(request: HttpRequest):

    data = json.loads(request.body)
    print(data)
    product_id = data.get('productId')
    options = data.get('options')
    final_price = data.get('price')

    _message = "Ошибка добавления товара в корзину"

    product = Products.objects.get(id=product_id)
    
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            for cart in carts:
                if cart and cart.options == options and cart.final_price == final_price:
                    cart.quantity += 1
                    cart.save()
                    break
            else: Cart.objects.create(user=request.user, product=product, quantity=1, options=options, final_price=final_price)
            _message = 'Товар добавлен в корзину'
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1, options=options, final_price=final_price)
            _message = 'Товар добавлен в корзину'

    else:
        carts = Cart.objects.filter(
            session_key=request.session.session_key, product=product)

        if carts.exists():
            for cart in carts:
                if cart and cart.options == options and cart.final_price == final_price:
                    cart.quantity += 1
                    cart.save()
                    break
            else: 
                Cart.objects.create(
                session_key=request.session.session_key, product=product, quantity=1, options=options, final_price=final_price)
            _message = "Товар добавлен в корзину"
        else:
            Cart.objects.create(
                session_key=request.session.session_key, product=product, quantity=1, options=options, final_price=final_price)
            _message = "Товар добавлен в корзину"
    
    #user_cart = get_user_carts(request)
    #cart_items_html = render_to_string(
    #    "carts/includes/included_cart.html", {"carts": user_cart}, request=request)

    response_data = {
        "message": _message,
        #"cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)


def cart_remove(request):
    ...


def cart_change(request):
    ...


