from django import template
from cart.utils import get_product_options, get_user_carts


register = template.Library()


@register.simple_tag()
def user_carts(request):
    return get_user_carts(request)

@register.simple_tag()
def product_options(cart):
    return get_product_options(cart)