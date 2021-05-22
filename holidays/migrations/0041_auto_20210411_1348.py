# Generated by Django 3.1.7 on 2021-04-11 08:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('holidays', '0040_auto_20210409_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='messagess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=80)),
                ('subject', models.CharField(default='', max_length=200)),
                ('messages', models.TextField()),
                ('messaged_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='affialiate_click',
            name='date_logged_in',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 18, 32, 14848, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='affiliate_info_user',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 18, 32, 14848, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='affiliate_success',
            name='date_affiliate_successfull',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 18, 32, 14848, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='affiliate_transaction',
            name='date_of_transaction',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 18, 32, 14848, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='affiliateaccounts',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 18, 32, 6715, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='affiliateinfo',
            name='date_edited',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 18, 32, 6715, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='banner',
            name='datecreated',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 18, 32, 6715, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='createdat',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 18, 32, 6715, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 18, 32, 6715, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='destinations',
            name='timecreated',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 18, 32, 6715, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 13, 48, 31, 997467)),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='hotel_updatedon',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 18, 31, 997467, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='offers',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 18, 31, 997467, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='offers',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 18, 31, 997467, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 18, 31, 997467, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderforpackage',
            name='date_ordered',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 18, 31, 997467, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='packages',
            name='package_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 18, 31, 997467, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='promo_used',
            name='used_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 18, 32, 6715, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 18, 32, 6715, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='datecreated',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 18, 32, 6715, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='services',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 18, 32, 6715, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transport',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 18, 32, 5523, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 18, 32, 5682, tzinfo=utc)),
        ),
    ]