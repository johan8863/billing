# Generated by Django 4.2 on 2023-04-22 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_order_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemtimes',
            name='times',
            field=models.PositiveIntegerField(default=1, verbose_name='Cantidad'),
        ),
    ]
