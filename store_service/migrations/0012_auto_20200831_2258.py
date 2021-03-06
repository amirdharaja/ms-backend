# Generated by Django 2.2.14 on 2020-08-31 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_service', '0011_auto_20200826_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('Home', 'Home'), ('Work', 'Work'), ('Other', 'Other')], max_length=8),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('COD', 'Cash On Delivery'), ('Wallet', 'Wallet'), ('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card')], default='COD', max_length=32),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('', '-------'), ('New', 'New'), ('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered'), ('Canceled by User', 'Canceled by User'), ('Canceled by Admin', 'Canceled by Admin'), ('Success', 'Success'), ('Failed', 'Failed')], default='pending', max_length=16),
        ),
        migrations.AlterField(
            model_name='refund',
            name='status',
            field=models.CharField(choices=[('', '-------'), ('Pending', 'Pending'), ('Paid', 'Paid')], default='pending', max_length=32),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='role',
            field=models.CharField(choices=[('', ''), ('User', 'User'), ('Admin', 'Admin'), ('Super Admin', 'Super Admin'), ('Delivery Boy', 'Delivery Boy')], default='User', max_length=16),
        ),
    ]
