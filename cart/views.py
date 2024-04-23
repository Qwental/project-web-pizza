import json
from django.http import JsonResponse
from django.shortcuts import render

from cart.models import Cart
from main.models import Products

def cart_add(request):

    data = json.loads(request.body)
    product_id = data['productId']
    #options = request.POST.get("options")

    product = Products.objects.get(id=product_id)
    
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            for cart in carts:
                if cart:
                    cart.quantity += 1
                    cart.save()
                    break
            else: Cart.objects.create(user=request.user, product=product, quantity=1)
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1, options={'a':'a'}, final_price=300)

    else:
        carts = Cart.objects.filter(
            session_key=request.session.session_key, product=product)

        if carts.exists():
            for cart in carts:
                if cart:
                    cart.quantity += 1
                    cart.save()
                    break
            else: 
                Cart.objects.create(
                session_key=request.session.session_key, product=product, quantity=1)
        else:
            Cart.objects.create(
                session_key=request.session.session_key, product=product, quantity=1)
    
    #user_cart = get_user_carts(request)
    #cart_items_html = render_to_string(
    #    "carts/includes/included_cart.html", {"carts": user_cart}, request=request)

    response_data = {
        "message": "Товар добавлен в корзину",
        #"cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)


def cart_remove(request):
    ...


def cart_change(request):
    ...