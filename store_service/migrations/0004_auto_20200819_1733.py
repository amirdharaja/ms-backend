# Generated by Django 2.2.14 on 2020-08-19 12:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_service', '0003_auto_20200819_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phoneotp',
            name='phone',
            field=models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message='Enter valid phone number', regex='^[3-9]\\d{9}$')]),
        ),
    ]