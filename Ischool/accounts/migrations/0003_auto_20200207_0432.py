# Generated by Django 3.0.1 on 2020-02-07 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200203_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 7, 4, 32, 31, 174530)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='date_registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 7, 4, 32, 31, 146567)),
        ),
    ]
