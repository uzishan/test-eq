from core.models import *
from rest_framework import serializers


class BuildingSerializer(serializers.HyperlinkedModelSerializer):
    location = serializers.CharField(source='location_address')
    avg_temperature = serializers.SerializerMethodField('_get_avg_temperature')

    class Meta:
        model = Building
        fields = ('pk',
                  'title',
                  'image_url',
                  'location',
                  'campus_name',
                  'avg_temperature')

    def _get_avg_temperature(self, obj):
        # magia filtrului per buildingu asta.
        return "media temperaturii pe buildingu asta!"


class FloorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Floor
        fields = ('number',
                  'title')