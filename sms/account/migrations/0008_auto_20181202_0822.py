# Generated by Django 2.1.3 on 2018-12-02 08:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20181126_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentfees',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 2, 8, 22, 2, 32184)),
        ),
    ]
