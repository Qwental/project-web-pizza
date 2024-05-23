# Generated by Django 4.2.11 on 2024-05-23 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_on_get',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Создан'), (1, 'Оплачен'), (2, 'В пути'), (3, 'Ожидает'), (4, 'Получен')], default=0),
        ),
    ]