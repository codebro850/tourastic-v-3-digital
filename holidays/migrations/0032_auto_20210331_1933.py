# Generated by Django 3.1.7 on 2021-03-31 14:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holidays', '0031_auto_20210331_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliateaccounts',
            name='aid',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 31, 19, 33, 45, 709312)),
        ),
    ]
