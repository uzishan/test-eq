from django.db import models


# Create your models here.

class Building(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    image_url = models.CharField(max_length=255)
    location_address = models.CharField(max_length=100)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    campus_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title


class Floor(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=30)
    plans_image_url = models.CharField(max_length=255)
    building = models.ForeignKey('Building', on_delete=models.CASCADE, related_name='floors')

    def __unicode__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'number')


class Room(models.Model):
    title = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    surface = models.CharField(max_length=30)
    floor = models.ForeignKey('Floor', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title


class Sensor(models.Model):
    SENSOR_TYPE_CHOICES = (

        ('TP', 'Temperature'),
        ('HU', 'Humidity'),
    )

    name = models.CharField(max_length=30)
    serial_no = models.IntegerField()
    type = models.CharField(max_length=30, choices=SENSOR_TYPE_CHOICES, default='TP')
    location = models.CharField(max_length=30)
    unit_of_measurement = models.CharField(max_length=10)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name


class SensorData(models.Model):
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE)
    timestamp = models.DateTimeField('Read date', auto_now=True)
    value = models.IntegerField()
