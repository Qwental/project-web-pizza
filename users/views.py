from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.db import transaction
from cart.models import Cart
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm
from users.models import Products
from orders.models import Order, OrderItem
from django.db.models import Prefetch
from django.contrib import auth, messages


def login(request):
    """
    Контроллер отвечающий за  авторизацию пользователя
    Сделан по документации
    """
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Логин',
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    """
    Контроллер отвечающий за регистрацию пользователя
    """
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()
                    session_key = request.session.session_key
                    user = form.instance
                    auth.login(request, user)
                    if session_key:
                        Cart.objects.filter(session_key=session_key).update(user=user)
                    return HttpResponseRedirect(reverse('main:index'))
            except Exception as e:
                print(str(e))
        else:
            print('form invalid')
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {
        "products": Products.objects.all(),
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)


@login_required
def logout(request):
    """
    Контроллер отвечающий за выход пользователя из аккаунта
    """
    auth.logout(request)
    return redirect(reverse('main:index'))


def lost_pass(request):
    """
    Контроллер отвечающий за функционал восстановления пароля
    """
    if request.method == 'POST':
        form = PasswordResetForm(data=request.POST)
        if form.is_valid():
            response_data = {'message': 'Письмо отправлено'}
            return JsonResponse(response_data)
    else:
        form = PasswordResetForm()

    context = {
        'title': 'Потерял пароль',
        'form': form,
    }
    return render(request, 'users/lost_pass.html', context)


@login_required
def profile(request):
    """
    Контроллер отвечающий за страницу с личным кабинетом, редактированием информации,
    просмотр истории заказов
    """
    if request.method == 'POST':
        with transaction.atomic():
            form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
            if form.is_valid():
                try:
                    with transaction.atomic():
                        form.save()
                        messages.success(request, "Профайл успешно обновлен")
                        return HttpResponseRedirect(reverse('user:profile'))
                except Exception as e:
                    print(str(e))
            else:
                print('form is invalid', form.errors)
    else:
        form = ProfileForm(instance=request.user)

    orders = Order.objects.filter(user=request.user).prefetch_related(
        Prefetch(
            "orderitem_set",
            queryset=OrderItem.objects.select_related("product"),
        )
    ).order_by("-id")
    products = request.user.favorite_products.all()

    context = {
        'title': 'Home - Кабинет',
        'products': Products.objects.all(),
        'form': form,
        'orders': orders,
        'products_favorite': products
    }
    return render(request, 'users/profile.html', context)
