# Generated by Django 3.1.7 on 2021-03-20 06:46

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('holidays', '0017_auto_20210316_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='affiliateaccounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=20)),
                ('email', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=100)),
                ('date_joined', models.DateTimeField(default=datetime.datetime(2021, 3, 20, 6, 46, 7, 951536, tzinfo=utc))),
            ],
        ),
        migrations.AlterField(
            model_name='blogs',
            name='createdat',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 20, 6, 46, 7, 949541, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 20, 6, 46, 7, 950539, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 20, 12, 16, 7, 946550)),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='hotel_updatedon',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 20, 6, 46, 7, 946550, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='offers',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 20, 6, 46, 7, 930249, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='offers',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 20, 6, 46, 7, 930249, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 20, 6, 46, 7, 930249, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderforpackage',
            name='date_ordered',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 20, 6, 46, 7, 930249, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='packages',
            name='package_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 20, 6, 46, 7, 930249, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transport',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 20, 6, 46, 7, 947547, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 20, 6, 46, 7, 948544, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='affiliateinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=100)),
                ('second_name', models.CharField(blank=True, default='', max_length=100)),
                ('mobile_number', models.IntegerField(default=0, max_length=12)),
                ('pincode', models.IntegerField(default=0, max_length=8)),
                ('state', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('country', models.CharField(default='', max_length=100)),
                ('address_temp', models.CharField(blank=True, default='', max_length=200)),
                ('date_edited', models.DateTimeField(default=datetime.datetime(2021, 3, 20, 6, 46, 7, 952533, tzinfo=utc))),
                ('affiliate_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='holidays.affiliateaccounts')),
            ],
        ),
    ]
