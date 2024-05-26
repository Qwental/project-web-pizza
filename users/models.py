from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pay_type = models.CharField(verbose_name='Тип оплаты', max_length=10)

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
