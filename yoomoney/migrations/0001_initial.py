# Generated by Django 5.1.2 on 2024-11-02 04:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('amount_value', models.DecimalField(decimal_places=2, max_digits=99)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name="payment's date")),
            ],
        ),
    ]
