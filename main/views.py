from django.shortcuts import render


def index(request):
    test_range = range(0, 12)
    return render(request, 'main/index.html', {'test_range': test_range})
