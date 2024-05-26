from django.shortcuts import render

# Create your views here.

from cart.views import *

from users.models import User

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render

from cart.models import Cart
from datetime import datetime, timedelta

from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem


def valid_intervals():
    orders = Order.objects.all()
    current_time = datetime.now().time()

    # Создаем словарь, где ключ - интервал, значение - текущая нагруженность на интервал
    start_time = (datetime.now()).replace(hour=9, minute=0)
    end_time = (datetime.now()).replace(hour=23, minute=20)
    pizza_work_time_start = (datetime.now()).replace(hour=9, minute=0)
    if ((datetime.now()).replace(hour=23, minute=0).time() < current_time < (datetime.now()).replace(hour=23,
                                                                                                     minute=59).time()) or (
            (datetime.now()).replace(hour=0, minute=0).time() < current_time < (datetime.now()).replace(hour=6,
                                                                                                        minute=0).time()):
        valid_intervals_arr = [
            'Нет свободных интервалов, пиццерия сейчас не работает!'
        ]
        return valid_intervals_arr

    intervals_load = {}
    for i in range(28):
        s = f'{start_time.strftime("%H:%M")}-'
        start_time = (start_time + timedelta(minutes=30))
        s += f'{start_time.strftime("%H:%M")}'
        intervals_load[s] = 0
    for order in orders:
        if order.get_status_display() != 'Получен':
            time_order = order.time_pickup_delivery
            # print(time_order)
            for key in intervals_load.keys():
                start_interval = datetime.strptime((str(str(key).split('-')[0])), "%H:%M").time()
                end_interval = datetime.strptime((str(str(key).split('-')[1])), "%H:%M").time()
                # print(start_interval, time_order, end_interval)
                if start_interval <= time_order <= end_interval:
                    intervals_load[key] += 1
    valid_intervals_arr = []

    for key in intervals_load.keys():
        start_interval = datetime.strptime((str(str(key).split('-')[0])), "%H:%M").time()
        end_interval = datetime.strptime((str(str(key).split('-')[1])), "%H:%M").time()
        if current_time < start_interval and end_interval > current_time:
            if intervals_load[key] < 5:
                valid_intervals_arr.append(key)

    # temp = valid_intervals_arr[0]
    # for interval in valid_intervals_arr:
    #     if temp == interval:

    return valid_intervals_arr


# Это для самовывоза
@login_required
def create_order_pickup(request):
    temp_cartContent = get_user_carts(request)
    form_errors = []
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        print('create_order_pickup')
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    # cart_items = Cart.objects.filter(user=user)
                    cartContent = get_user_carts(request)
                    if cartContent.exists():
                        # Создать заказ
                        order = Order.objects.create(
                            user=user,
                            requires_delivery=0,
                            delivery_address='Самовывоз',
                            time_pickup_delivery=form.clean_my_time(0),
                            email=form.cleaned_data['email'],
                            cash_payment=form.cleaned_data['cash_payment'],
                            is_paid=form.clean_paid(),
                            status=form.clean_paid(),
                        )

                        # Создать заказанные товары
                        for cart_item in cartContent:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.final_price
                            quantity = cart_item.quantity
                            options = cart_item.options

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                                options=options,
                            )
                            product.save()

                        # Очистить корзину пользователя после создания заказа
                        cartContent.delete()
                        messages.success(request, 'Заказ оформлен!')
                        return redirect('orders:success')
            except ValidationError as e:
                print(str(e))
                form_errors = e.messages
                # messages.success(request, str(e))
                # return redirect('orders:create_order_pickup')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        form = CreateOrderForm(initial=initial)




    context = {
        'valid_intervals_arr': valid_intervals(),
        'cash_payment': request.user.cash_payment,
        'user_email': request.user.email,
        'title': 'Оформление заказа',
        'form': form,
        'form_errors': form_errors,
        'orders': True,
        "cartContent": temp_cartContent,
    }
    return render(request, 'orders/create_order_pickup.html', context=context)


# Это для Доставки
@login_required
def create_order(request):
    temp_cartContent = get_user_carts(request)
    form_errors = []
    print('create_order')
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            print('form.is_valid')
            try:
                with transaction.atomic():
                    user = request.user
                    # cart_items = Cart.objects.filter(user=user)
                    cartContent = get_user_carts(request)
                    if cartContent.exists():
                        # Создать заказ

                        order = Order.objects.create(
                            user=user,
                            requires_delivery=1,
                            delivery_address=form.cleaned_data['delivery_address'],
                            time_pickup_delivery=form.clean_my_time(1),
                            email=form.cleaned_data['email'],
                            cash_payment=form.cleaned_data['cash_payment'],
                            is_paid=form.clean_paid(),
                            status=form.clean_paid(),
                        )
                        print(order)
                        # Создать заказанные товары
                        for cart_item in cartContent:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.final_price
                            quantity = cart_item.quantity
                            options = cart_item.options

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                                options=options,
                            )
                            product.save()
                        # Очистить корзину пользователя после создания заказа
                        cartContent.delete()
                        messages.success(request, 'Заказ оформлен!')
                        return redirect('orders:success')
            except ValidationError as e:
                form_errors = e.messages
                print(str(e), e.messages, 'mistake')
                #messages.success(request, str(e))
                #return redirect('orders:create_order')
        else:
            print('form инвалид')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,

        }
        form = CreateOrderForm(initial=initial)
        print('mistake2')

    context = {
        'title': 'Оформление заказа',
        'cash_payment': request.user.cash_payment,
        'valid_intervals_arr': valid_intervals(),
        'user_email': request.user.email,
        'form': form,
        'form_errors': form_errors,
        'orders': True,
        "cartContent": temp_cartContent,
    }
    return render(request, 'orders/create_order.html', context=context)


def success(request):
    return render(request, 'orders/success.html')


def delivery_or_pickup(request):
    return render(request, 'orders/delivery_or_pickup.html')
