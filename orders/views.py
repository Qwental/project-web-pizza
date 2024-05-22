from django.shortcuts import render


# Create your views here.

from cart.views import *


def create_order(request):
    cartContent = get_user_carts(request)
    context = {
        "cartContent": cartContent,
    }
    return render(request, 'orders/create_order.html', context=context)
