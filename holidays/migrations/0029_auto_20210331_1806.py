# Generated by Django 3.1.7 on 2021-03-31 12:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holidays', '0028_auto_20210330_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 31, 18, 6, 37, 448291)),
        ),
    ]
