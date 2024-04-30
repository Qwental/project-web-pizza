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
    options_dict = {}
    options_dict['adds'] = [opt[:opt.find(':')] for opt in options.get('add')]
    del options['add']
    options_dict['params'] = []
    for item in options.items():
        options_dict['params'].append(item)
    return options_dict

