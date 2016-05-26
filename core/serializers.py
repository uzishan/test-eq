from core.models import *
from rest_framework import serializers, filters
from random import randint
from django.db.models import Avg


class BuildingSerializer(serializers.HyperlinkedModelSerializer):
    location = serializers.CharField(source='location_address')
    avg_temperature = serializers.SerializerMethodField('_get_avg_temperature')
    avg_humidity = serializers.SerializerMethodField('_generate_occupancy_level')
    occupancy_level = serializers.SerializerMethodField('o_c')

    class Meta:
        model = Building
        fields = ('pk',
                  'title',
                  'image_url',
                  'location',
                  'campus_name',
                  'avg_temperature',
                  'avg_humidity',
                  'occupancy_level')

    def _get_avg_temperature(self, obj):
        # magia filtrului per buildingu asta.
        sensors = Sensor.objects.all()
        avgt = 0
        # avgh = 0
        while obj.pk:
            for s in sensors:
                if s.type == "temperature":
                    avgt = avgt + s.value

                # elif s.type == "humidity":
                   # avgh = avgh + s.value

        avgt = avgt / 2

        # avgh = avgh / 2
        return avgt
            # SensorData.objects.ilter(sensor__type="temperature").aggregate(Avg('value'))

    def _get_avg_humidity(self, obj):
        # magia filtrului per buildingu asta.
        return SensorData.objects.filter(sensor__type="humidity").aggregate(Avg('value'))

    def _generate_occupancy_level(self, obj):
        ocup = randint(45, 65)
        return ocup


class FloorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Floor
        fields = ('number',
                  'title')
