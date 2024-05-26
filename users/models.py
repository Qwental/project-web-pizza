from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    CARD = 0
    CASH = 1

    STATUSES = (
        (CARD, 'Карта'),
        (CASH, 'Наличные'),
    )

    status = models.SmallIntegerField(default=CARD, choices=STATUSES)

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
