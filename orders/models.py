# Create your models here.


from django.db import models

# from goods.models import Products

from main.models import Products

from users.models import User
from cart.models import *

from orders.utils import default_start_time


class OrderitemQueryset(models.QuerySet):
    """
    Данный класс нужен для того, чтобы мы могли получать
    полную сумму total_price в заказе и количество продуктов total_quantity в заказе
    """

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Order(models.Model):
    """
    Класс Заказа
    """

    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name="Пользователь",
                             default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True,
                                             verbose_name="Дата создания заказа")
    #Статусы заказа
    CREATED = 0
    PAID = 1
    ON_WAY = 2
    WAITING = 3
    DELIVERED = 4
    STATUSES = (
        (CREATED, 'Создан'),
        (PAID, 'Оплачен'),
        (ON_WAY, 'В пути'),
        (WAITING, 'Ожидает'),
        (DELIVERED, 'Получен'),
    )
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)
    requires_delivery = models.BooleanField(default=False, verbose_name="Требуется доставка")
    delivery_address = models.TextField(null=True, blank=True, verbose_name="Адрес доставки",
                                        default='Пользователь выбрал самовывоз', )
    is_paid = models.BooleanField(default=False, verbose_name="Заказ оплачен")
    time_pickup_delivery = models.TimeField(default=default_start_time, verbose_name="Время доставки/самовывоза")
    email = models.EmailField(max_length=256, blank=True, null=True,
                              verbose_name="Почтовый ящик", default='default@example.com')

    # Добавлен способ оплаты в Заказе
    CARD_PAYMENT = 0
    CASH_PAYMENT = 1
    PAYMENT_VARIATIONS = (
        (CARD_PAYMENT, 'Оплата картой'),
        (CASH_PAYMENT, 'Оплата наличными'),
    )
    cash_payment = models.SmallIntegerField(default=CARD_PAYMENT, choices=PAYMENT_VARIATIONS,
                                            verbose_name='Способ оплаты')

    class Meta:
        db_table = "order"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ № {self.pk} | Покупатель {self.user.first_name} {self.user.last_name}"


class OrderItem(models.Model):
    """
    Класс продукта в Заказе
    """
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(to=Products, on_delete=models.SET_DEFAULT, null=True, verbose_name="Продукт",
                                default=None)
    name = models.CharField(max_length=150, verbose_name="Название")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажи")
    options = JSONField(verbose_name='Дополнительные параметры', schema=OPTIONS_SCHEMA,
                        default=dict)

    class Meta:
        db_table = "order_item"
        verbose_name = "Проданный товар"
        verbose_name_plural = "Проданные товары"

    objects = OrderitemQueryset.as_manager()

    def products_price(self):
        return round(self.price * self.quantity, 2)

    def original_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f"Товар {self.name} | Заказ № {self.order.pk}"
