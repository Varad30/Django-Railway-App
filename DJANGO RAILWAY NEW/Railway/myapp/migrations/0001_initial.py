# Generated by Django 4.0.4 on 2022-11-04 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rain_No', models.IntegerField()),
                ('train_name', models.CharField(max_length=100)),
            ],
        ),
    ]
