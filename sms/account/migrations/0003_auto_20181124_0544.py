# Generated by Django 2.1.3 on 2018-11-24 05:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_payment_studentfees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentfees',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 24, 5, 44, 48, 842857)),
        ),
    ]
