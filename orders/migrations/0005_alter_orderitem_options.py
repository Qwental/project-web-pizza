# Generated by Django 4.2.11 on 2024-05-23 17:15

from django.db import migrations
import django_jsonform.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_orderitem_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='options',
            field=django_jsonform.models.fields.JSONField(default=dict, verbose_name='Дополнительные параметры'),
        ),
    ]
