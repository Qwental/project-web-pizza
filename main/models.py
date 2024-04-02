from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=150, unique=True, verbose_name="Название категории"
    )
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    @property
    def get_products(self):
        """
        Возвращает список всех товаров данной категории.
        Используется для заполнения товаров по категориям в меню.
        """
        return Products.objects.filter(category=self.id)


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена"
    )
    discount = models.DecimalField(
        default=0.00, max_digits=4, decimal_places=2, verbose_name="Скидка в %"
    )
    category = models.ForeignKey(
        to=Category,
        related_name="products",
        on_delete=models.CASCADE,
        verbose_name="Категория",
    )
    available = models.BooleanField(default=True, verbose_name="Наличие")
    image = models.ImageField(
        upload_to="product_images", blank=True, null=True, verbose_name="Изображение"
    )
    # Вань, так как это всё на фронт передовать будем? Шаблон для выбора параметра товара, получается, разный 🤔
    options = models.CharField(
        max_length=1000, blank=True
    )  # для записи параметров товара, например (('размер',('S','M','L')), ('тесто',('тонкое','толстое')))
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("id",)

    def __str__(self):
        return f"{self.name}"

    def sell_price(self):
        """
        Возвращает итоговую цену товара с подсчётом скидки.
        """
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
