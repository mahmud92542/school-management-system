# Generated by Django 2.1.3 on 2018-12-03 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20181203_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentfees',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 3, 16, 25, 8, 393292)),
        ),
    ]
