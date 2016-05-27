from random import randint

from django.core.management import BaseCommand

from core.models import *


class Command(BaseCommand):
    help = 'Simulates data collection for Humidity and Temperature sensors'

    def handle(self, *args, **options):

        sensors = Sensor.objects.all()

        for s in sensors:
            val = 0
            if s.type == Sensor.SENSOR_TYPE_CHOICES['TP']:
                val = randint(18, 28)
            elif s.type == Sensor.SENSOR_TYPE_CHOICES['HU']:
                val = randint(30, 70)
            sensor_data = SensorData(sensor=s, value=val)
            sensor_data.save()
