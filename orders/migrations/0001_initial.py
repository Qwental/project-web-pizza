# Generated by Django 4.2.11 on 2024-05-27 11:24

from django.db import migrations, models
import django.db.models.deletion
import django_jsonform.models.fields
import orders.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')),
                ('status', models.SmallIntegerField(choices=[(0, 'Создан'), (1, 'Оплачен'), (2, 'В пути'), (3, 'Ожидает'), (4, 'Получен')], default=0)),
                ('requires_delivery', models.BooleanField(default=False, verbose_name='Требуется доставка')),
                ('delivery_address', models.TextField(blank=True, default='Пользователь выбрал самовывоз', null=True, verbose_name='Адрес доставки')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Заказ оплачен')),
                ('time_pickup_delivery', models.TimeField(default=orders.utils.default_start_time, verbose_name='Время доставки/самовывоза')),
                ('email', models.EmailField(blank=True, default='default@example.com', max_length=256, null=True, verbose_name='Почтовый ящик')),
                ('cash_payment', models.SmallIntegerField(choices=[(0, 'Оплата картой'), (1, 'Оплата наличными')], default=0, verbose_name='Способ оплаты')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата продажи')),
                ('options', django_jsonform.models.fields.JSONField(default=dict, verbose_name='Дополнительные параметры')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.products', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Проданный товар',
                'verbose_name_plural': 'Проданные товары',
                'db_table': 'order_item',
            },
        ),
    ]
