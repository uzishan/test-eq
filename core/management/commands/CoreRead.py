
from django.core.management.base import BaseCommand, CommandError
from core.models import SensorData

class Command(BaseCommand)
    help = 'Simulates data collection for Humidity and Temperature sensors'


     def sensor_temp(self):
         t.randint(10,30)

         temperature = t+ "c"

            f= open('workfile', 'w')

            print (f temperature)


    def sensor_humid(self):

        h.randint(10, 30)

        humidity = h + "c"

         f = open('workfile', 'w')

         print( f humidity)

    #workfile is a placeholder name