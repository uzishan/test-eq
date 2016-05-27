from core.models import *
from rest_framework import serializers, filters
from random import randint
from django.db.models import Avg


class BuildingSerializer(serializers.HyperlinkedModelSerializer):
    location = serializers.CharField(source='location_address')
    avg_temperature = serializers.SerializerMethodField('_get_avg_temperature')
    avg_humidity = serializers.SerializerMethodField('_generate_occupancy_level')
    occupancy_level = serializers.SerializerMethodField('_generate_occupancy_level')

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
        temp = SensorData.objects.filter(sensor__room__floor__building__pk=obj.pk).filter(sensor__type='TP')\
            .aggregate(Avg('value'))
        return temp

    def _get_avg_humidity(self, obj):
        # magia filtrului per buildingu asta.
        hum = SensorData.objects.filter(sensor__room__floor__building__pk=obj.pk).filter(sensor__type='TP')\
            .aggregate(Avg('value'))
        return hum

    def _generate_occupancy_level(self, obj):
        ocup = randint(45, 65)
        return ocup


class FloorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Floor
        fields = ('number',
                  'title')
