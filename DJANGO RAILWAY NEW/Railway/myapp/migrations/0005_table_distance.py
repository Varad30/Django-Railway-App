# Generated by Django 4.0.4 on 2022-11-04 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_table_arrival_time_alter_table_departure_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='distance',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
