# Generated by Django 4.0.4 on 2022-11-04 17:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_rain_no_table_train_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='arrival_time',
            field=models.TimeField(auto_now_add=True, default=datetime.datetime(2022, 11, 4, 17, 44, 35, 617570, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='table',
            name='departure_time',
            field=models.TimeField(auto_now_add=True, default=datetime.datetime(2022, 11, 4, 17, 44, 44, 359513, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='table',
            name='destination_station_name',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='table',
            name='station_name',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
    ]