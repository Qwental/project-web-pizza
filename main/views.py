from unicodedata import category
from django.shortcuts import render

from main.models import Category


def index(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'main/index.html', context=context)
