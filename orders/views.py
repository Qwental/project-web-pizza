from django.shortcuts import render

# Create your views here.

from cart.views import *

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render

from cart.models import Cart

from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem


@login_required
def create_order(request):
    temp_cartContent = get_user_carts(request)

    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    # cart_items = Cart.objects.filter(user=user)

                    cartContent = get_user_carts(request)

                    if cartContent.exists():
                        # Создать заказ
                        # email=form.cleaned_data['email'],
                        order = Order.objects.create(
                            user=user,
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )
                        # Создать заказанные товары
                        for cart_item in cartContent:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.final_price
                            quantity = cart_item.quantity


                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.save()

                        # Очистить корзину пользователя после создания заказа
                        cartContent.delete()

                        messages.success(request, 'Заказ оформлен!')
                        return redirect('orders:success')

            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('cart:cart_view')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }

        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Home - Оформление заказа',
        'form': form,
        'orders': True,
        "cartContent": temp_cartContent,
    }
    return render(request, 'orders/create_order.html', context=context)


def success(request):
    return render(request, 'orders/success.html')