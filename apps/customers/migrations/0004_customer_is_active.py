# Generated by Django 4.1.7 on 2023-04-02 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_customer_bank_account_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_active',
            field=models.BooleanField(default=True, editable=False),
        ),
    ]