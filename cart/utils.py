import json
from cart.models import Cart



def get_user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user).select_related('product')
    
    if not request.session.session_key:
        request.session.create()
    return Cart.objects.filter(session_key=request.session.session_key).select_related('product')


def get_product_options(cart: Cart):
    options = cart.options
    options_list = []
    options_list.append(options['add'])
    del options['add']
    options_list.append([])
    for item in options.items():
        options_list[1].append(item)
    return options_list

