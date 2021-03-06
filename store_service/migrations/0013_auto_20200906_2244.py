# Generated by Django 2.2.14 on 2020-09-06 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_service', '0012_auto_20200831_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('COD', 'Cash On Delivery'), ('Wallet', 'Wallet'), ('Card', 'Card')], default='COD', max_length=32),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('', '-------'), ('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], default='Pending', max_length=16),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
