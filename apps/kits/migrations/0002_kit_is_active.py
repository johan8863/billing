# Generated by Django 4.1.7 on 2023-04-02 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kit',
            name='is_active',
            field=models.BooleanField(default=True, editable=False),
        ),
    ]
