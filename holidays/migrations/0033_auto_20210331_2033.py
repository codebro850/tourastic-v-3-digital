# Generated by Django 3.1.7 on 2021-03-31 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holidays', '0032_auto_20210331_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliateaccounts',
            name='aid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 31, 20, 33, 1, 671743)),
        ),
    ]
