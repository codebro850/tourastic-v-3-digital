# Generated by Django 3.1.7 on 2021-03-16 09:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('holidays', '0014_auto_20210315_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='createdat',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 16, 9, 21, 28, 228799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 16, 9, 21, 28, 228799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 16, 14, 51, 28, 228799)),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='hotel_updatedon',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 16, 9, 21, 28, 228799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 16, 9, 21, 28, 213186, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderforpackage',
            name='date_ordered',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 16, 9, 21, 28, 213186, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='packages',
            name='package_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 16, 9, 21, 28, 213186, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transport',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 16, 9, 21, 28, 228799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 16, 9, 21, 28, 228799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='mobile_no',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.BooleanField(default=False)),
                ('discount_percentage', models.IntegerField(default=0)),
                ('valid_to', models.DateTimeField(default=datetime.datetime(2021, 3, 16, 9, 21, 28, 228799, tzinfo=utc))),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 3, 16, 9, 21, 28, 228799, tzinfo=utc))),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='holidays.packages')),
            ],
        ),
    ]
