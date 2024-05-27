from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django_jsonform.models.fields import JSONField
from django.conf import settings
from main.models import Addition, Products

User = settings.AUTH_USER_MODEL


class CartQueryset(models.QuerySet):
    """
    Класс нужный для нахождения суммарной цены total_price и количества товаров total_quantity с использованием QuerySet
    """

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


def OPTIONS_SCHEMA():
    """
    Схема для продуктов в корзине
    """
    schema = {
        "type": "dict",
        "title": "Дополнительные характеристики",
        "keys": {
            "add": {
                "type": "array",
                "title": "Добавки",
                "items": {
                    "type": "string",
                    "choices": [f'{x.name}:{x.price}' for x in Addition.objects.all()],
                    "widget": "multiselect"
                }
            }
        },
        "additionalProperties": {
            "type": "string"
        }
    }
    return schema


class Cart(models.Model):
    """
    Класс Корзины
    """
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Товар')
    final_price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Конечная цена")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    options = JSONField(verbose_name='Дополнительные параметры', schema=OPTIONS_SCHEMA)

    class Meta:
        db_table = 'cart'
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

    objects = CartQueryset().as_manager()

    def products_price(self):
        """
        Функция для нахождения итоговой цены и округления ее
        """
        return round(self.final_price * self.quantity, 2)

    def __str__(self):
        if self.user:
            return f'Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}'

        return f'Анонимная корзина | Товар {self.product.name} | Количество {self.quantity}'


class Coupon(models.Model):
    """
    Класс Промокод(Купон)
    """
    code = models.CharField(max_length=50, unique=True, verbose_name='Промокод')
    valid_from = models.DateTimeField(verbose_name='Активен c')
    valid_to = models.DateTimeField(verbose_name='Активен до')
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name='Скидка в %')
    active = models.BooleanField(verbose_name='Активен')

    class Meta:
        verbose_name = "Купон"
        verbose_name_plural = "Купоны"

    def __str__(self):
        return self.code
