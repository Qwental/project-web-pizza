# Generated by Django 4.2.11 on 2024-04-07 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_products_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Добавку',
                'verbose_name_plural': 'Добавки',
                'db_table': 'addition',
            },
        ),
    ]