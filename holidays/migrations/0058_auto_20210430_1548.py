# Generated by Django 3.1.7 on 2021-04-30 10:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('holidays', '0057_auto_20210428_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliate_info_user',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 10, 18, 46, 469929, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='affiliate_success',
            name='date_affiliate_successfull',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 10, 18, 46, 468816, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='affiliate_transaction',
            name='date_of_transaction',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 10, 18, 46, 469929, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='affiliateaccounts',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 10, 18, 46, 459251, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='affiliateinfo',
            name='date_edited',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 10, 18, 46, 459251, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='banner',
            name='datecreated',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 10, 18, 46, 459251, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='createdat',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 10, 18, 46, 459251, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 10, 18, 46, 459251, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='destinations',
            name='timecreated',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 10, 18, 46, 459251, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 15, 48, 46, 453814)),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='hotel_updatedon',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 10, 18, 46, 453814, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='offers',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 10, 18, 46, 453814, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='offers',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 10, 18, 46, 453814, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 10, 18, 46, 453814, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderforpackage',
            name='date_ordered',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 10, 18, 46, 453814, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='packages',
            name='package_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 10, 18, 46, 452788, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 10, 18, 46, 466348, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='datecreated',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 10, 18, 46, 459251, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='services',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 10, 18, 46, 459251, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transport',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 10, 18, 46, 458251, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 10, 18, 46, 458251, tzinfo=utc)),
        ),
    ]
