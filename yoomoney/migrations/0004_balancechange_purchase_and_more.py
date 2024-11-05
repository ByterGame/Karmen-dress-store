# Generated by Django 5.1.2 on 2024-11-02 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoomoney', '0003_rename_date_joined_balancechange_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='balancechange',
            name='purchase',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='balancechange',
            name='amount_value',
            field=models.IntegerField(max_length=100),
        ),
    ]