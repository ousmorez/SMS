# Generated by Django 3.0.6 on 2020-06-01 07:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200208_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 1, 12, 28, 29, 269306)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='date_registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 1, 12, 28, 29, 268309)),
        ),
    ]
