# Generated by Django 4.2.11 on 2024-05-27 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_products_description_alter_products_name_and_more'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favorite_products',
            field=models.ManyToManyField(blank=True, default=dict, null=True, to='main.products', verbose_name='Любимые продукты'),
        ),
    ]
