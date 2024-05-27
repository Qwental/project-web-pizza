from django.db import models
from django.contrib.auth.models import AbstractUser

from main.models import Products


class User(AbstractUser):
    CARD_PAYMENT = 0
    CASH_PAYMENT = 1
    PAYMENT_VARIATIONS = (
        (CARD_PAYMENT, 'Оплата картой'),
        (CASH_PAYMENT, 'Оплата наличными'),
    )
    cash_payment = models.SmallIntegerField(default=CARD_PAYMENT, choices=PAYMENT_VARIATIONS,
                                            verbose_name='Способ оплаты')

    favorite_products = models.ManyToManyField(Products, verbose_name='Любимые продукты', blank=True, null=True,
                                               default=dict)

    # ЭТА ИЗ-ЗА ЧЕГО НЕ РАБОТАЛО У МАКСИМА ВСЕ...... какая мета...
    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
