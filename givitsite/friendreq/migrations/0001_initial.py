# Generated by Django 3.1 on 2020-08-25 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemRequest',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('special_req', models.TextField()),
            ],
        ),
    ]
