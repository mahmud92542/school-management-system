# Generated by Django 2.1.3 on 2018-11-26 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20181126_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='student_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.StudentClass'),
        ),
        migrations.DeleteModel(
            name='StudentClass',
        ),
    ]