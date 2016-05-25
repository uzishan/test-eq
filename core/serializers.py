from core.models import *
from rest_framework import serializers
from random import randint
from django.db.models import Avg


class BuildingSerializer(serializers.HyperlinkedModelSerializer):
    location = serializers.CharField(source='location_address')
    avg_temperature = serializers.SerializerMethodField('_get_avg_temperature')
    avg_humidity = serializers.SerializerMethodField('_get_avg_humidity')
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
        t = SensorData.objects.filter(Building_id__in=Building.pk).filter(Sensor_type="temperature").aggregate(Avg('value'))
        return t

    def _get_avg_humidity(self, obj):
        # magia filtrului per buildingu asta.
        h = obj.SensorData.objects.filter(Building_id__in=Building.pk).filter(Sensor_type="humidity").aggregate(Avg('value'))
        return h

    def o_c(self, obj):
        ocup = obj.randint(45, 65)
        return ocup


class FloorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Floor
        fields = ('number',
                  'title')
