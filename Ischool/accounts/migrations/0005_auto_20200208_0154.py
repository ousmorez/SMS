# Generated by Django 3.0.1 on 2020-02-08 09:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200208_0152'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MYclass',
            new_name='Myclas',
        ),
        migrations.AlterField(
            model_name='student',
            name='date_registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 8, 1, 54, 33, 372857)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='date_registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 8, 1, 54, 33, 372857)),
        ),
    ]
