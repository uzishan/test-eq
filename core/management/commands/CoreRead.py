from random import randint

from django.core.management import BaseCommand

from core.models import *


class Command(BaseCommand):
    help = 'Simulates data collection for Humidity and Temperature sensors'

    def handle(self):
            for Sensor.id in range(0, 1000):
                if Sensor.type == "temperature":
                    return Sensor.SensorData.value(randint(20, 40))
                else:
                    return Sensor.SensorData.value(randint(5, 10))
