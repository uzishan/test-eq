from django.db import models


# Create your models here.

class Building(models.Model):
    title = models.CharField(max_length=30)

    def __unicode__(self):
        return self.title
    description = models.CharField(max_length=50)
    image_url = models.CharField(max_length=255)
    location_address = models.CharField(max_length=100)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    campus_name = models.CharField(max_length=255)


class Floor(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=30)

    def __unicode__(self):
        return self.title
    plans_image_url = models.CharField(max_length=255)
    building = models.ForeignKey('Building', on_delete=models.CASCADE)


class Room(models.Model):
    title = models.CharField(max_length=30)

    def __unicode__(self):
        return self.title
    type = models.CharField(max_length=30)
    surface = models.CharField(max_length=30)
    floor = models.ForeignKey('Floor', on_delete=models.CASCADE)


class Sensor(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name
    serial_no = models.IntegerField()
    type = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    unit_of_measurement = models.CharField(max_length=10)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)


class SensorData(models.Model):
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE)
    timestamp = models.DateTimeField('Read date', auto_now=True)
    value = models.IntegerField()
