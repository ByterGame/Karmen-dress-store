# Generated by Django 5.1.2 on 2024-10-22 10:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DressCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('color', models.CharField(max_length=256)),
                ('length', models.CharField(max_length=256)),
                ('material', models.CharField(max_length=256)),
                ('photo', models.ImageField(upload_to='products_images')),
                ('model', models.CharField(max_length=256)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.dresscategory')),
            ],
        ),
    ]
