# Generated by Django 5.1.2 on 2024-10-29 06:13

import contextlib
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dress',
            name='photo_hover',
            field=models.ImageField(default=contextlib.nullcontext, upload_to='products_images'),
        ),
    ]