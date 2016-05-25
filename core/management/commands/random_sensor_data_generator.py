from random import randint

from django.core.management import BaseCommand

from core.models import *


class Command(BaseCommand):
    help = 'Simulates data collection for Humidity and Temperature sensors'

    def handle(self):

        sensors = Sensor.objects.all()

        for s in sensors:
            if s.type == "temperature":

                val = randint(18, 28)

                sensor_data = SensorData(Sensor=s, value=val)
                sensor_data.save()

            else:

                val = randint(30, 70)
                sensor_data = SensorData(Sensor=s, value=val)
                sensor_data.save()
