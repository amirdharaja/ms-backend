# Generated by Django 2.2.14 on 2020-08-25 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_service', '0010_mainslideimage_subslideimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='rate',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='itemcategory',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]