import json
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from cart.models import Cart
from cart.utils import get_user_carts
from main.models import Products



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
        if not request.session.session_key:
            request.session.create()
            
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



def cart_change(request):
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")

    cart = Cart.objects.get(id=cart_id)

    cart.quantity = quantity
    cart.save()
    updated_quantity = cart.quantity

    cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "cart/components/cart_dynamic.html", {"cartContent": cart}, request=request)

    response_data = {
        # "message": "Количество изменено",
        "cart_items_html": cart_items_html,
        "quantity": updated_quantity,
    }

    return JsonResponse(response_data)



def cart_remove(request):
    
    cart_id = request.POST.get("cart_id")

    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "cart/components/cart_dynamic.html", {"cartContent": user_cart}, request=request)

    response_data = {
        # "message": "Товар удален",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)


def cart(request):
    '''
    Просто открывает страничку с корзиной
    '''

    cartContent = get_user_carts(request)

    context = {
        "cartContent": cartContent,
    }
    return render(request, 'cart/index.html', context=context)
