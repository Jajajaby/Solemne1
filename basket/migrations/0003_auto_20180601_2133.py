# Generated by Django 2.0.4 on 2018-06-02 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_auto_20180601_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
