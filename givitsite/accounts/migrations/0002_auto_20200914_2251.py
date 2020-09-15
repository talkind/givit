# Generated by Django 3.1.1 on 2020-09-14 19:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address_house_number',
            field=models.CharField(max_length=3, validators=[django.core.validators.RegexValidator(message='Please enter a valid number from 1 to 999.', regex='[0-9]{1-3}')], verbose_name='home_number'),
        ),
    ]
