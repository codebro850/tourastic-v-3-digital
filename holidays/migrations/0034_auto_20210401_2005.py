# Generated by Django 3.1.7 on 2021-04-01 14:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('holidays', '0033_auto_20210331_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 1, 20, 5, 45, 626899)),
        ),
        migrations.CreateModel(
            name='affiliate_transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount_withdrawn', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('ammount_left', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('transaction_id', models.CharField(default='', max_length=100)),
                ('date_of_transaction', models.DateTimeField(auto_now_add=True)),
                ('affliateuser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='holidays.affiliateaccounts')),
            ],
        ),
        migrations.CreateModel(
            name='affiliate_success',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount_received', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('ammount_earned_affiliate', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('percentage_affiliate', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5)),
                ('date_affiliate_successfull', models.DateTimeField(auto_now_add=True)),
                ('affiliate_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='holidays.packages')),
                ('affiliateuser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='holidays.affiliateaccounts')),
                ('successful_affiliate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='affiliate_info_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visited', models.IntegerField(default=0)),
                ('logged_in_users', models.IntegerField(default=0)),
                ('successfull_affiliate', models.IntegerField(default=0)),
                ('ammount_received', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('ammount_withdrawn', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('affliateuser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='holidays.affiliateaccounts')),
            ],
        ),
        migrations.CreateModel(
            name='affialiate_click',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_loged_in', models.DateTimeField(blank=True)),
                ('date_visited', models.DateTimeField(auto_now_add=True)),
                ('affliateuser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='holidays.affiliateaccounts')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
