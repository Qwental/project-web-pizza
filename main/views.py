from django.shortcuts import render

from main.models import Products


def index(request):
    products = Products.objects.filter()

    context = {
        'products': products,
    }
    return render(request, 'main/index.html', context=context)
