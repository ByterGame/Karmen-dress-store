# Generated by Django 5.1.2 on 2024-11-02 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoomoney', '0004_balancechange_purchase_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balancechange',
            name='purchase',
            field=models.CharField(default='', max_length=9999),
        ),
    ]
