# Generated by Django 4.2.11 on 2024-04-08 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_addition'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialOffers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.products', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Специальные предложения',
                'db_table': 'special_offer',
            },
        ),
    ]
