
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_jsonform.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),

    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Промокод')),
                ('valid_from', models.DateTimeField(verbose_name='Активен c')),
                ('valid_to', models.DateTimeField(verbose_name='Активен до')),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Скидка в %')),
                ('active', models.BooleanField(verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Купон',
                'verbose_name_plural': 'Купоны',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Конечная цена')),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='Количество')),
                ('session_key', models.CharField(blank=True, max_length=32, null=True)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('options', django_jsonform.models.fields.JSONField(verbose_name='Дополнительные параметры')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.products', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзина',
                'db_table': 'cart',
            },
        ),
    ]
