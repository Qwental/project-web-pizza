# Generated by Django 4.2.11 on 2024-05-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cash_payment',
            field=models.SmallIntegerField(choices=[(0, 'Оплата картой'), (1, 'Оплата наличными')], default=0),
        ),
    ]
