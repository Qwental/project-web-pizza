from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm

def login(request):
    #Метод из документации обработки с кнопкой войти
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'aboba',
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'aboba'
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'aboba'
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    ...
