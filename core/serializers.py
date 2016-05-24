from core.models import *
from rest_framework import serializers


class BuildingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Building
        fields = ('pk',
                  'title',
                  'image_url',
                  'location',
                  'campus_name')


class FloorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Floor
        fields = ('number',
                  'title')