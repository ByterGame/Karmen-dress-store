# Generated by Django 5.1.2 on 2024-11-05 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_dress_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='dress',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
