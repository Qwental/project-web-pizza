# Generated by Django 4.2.11 on 2024-05-23 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_remove_order_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='Оплачено'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_on_get',
            field=models.BooleanField(default=False, verbose_name='Оплата при получении'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_address',
            field=models.TextField(blank=True, default='Пользователь выбрал самовывоз', null=True, verbose_name='Адрес доставки'),
        ),
    ]
