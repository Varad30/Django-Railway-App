# Generated by Django 4.0.4 on 2022-11-04 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_table_arrival_time_table_departure_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='arrival_time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='departure_time',
            field=models.TimeField(blank=True),
        ),
    ]
