from django.db import models

# Create your models here.
class Table(models.Model):
    train_No=models.IntegerField()
    train_name=models.CharField(max_length=100)
    station_name=models.CharField(max_length=100)
    arrival_time=models.TimeField(blank=True)
    departure_time=models.TimeField(blank=True)
    destination_station_name=models.CharField(max_length=100)
    distance=models.IntegerField()
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.train_name