# Generated by Django 4.2.11 on 2024-05-26 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='pay_type',
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Карта'), (1, 'Наличные')], default=0),
        ),
    ]
