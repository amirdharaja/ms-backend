# Generated by Django 2.2.14 on 2020-08-24 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_service', '0009_auto_20200824_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainSlideImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/main_slide_images')),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'main_slide_images',
            },
        ),
        migrations.CreateModel(
            name='SubSlideImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default='images/no_image.png', upload_to='images/sub_slide_images')),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'sub_slide_images',
            },
        ),
    ]
