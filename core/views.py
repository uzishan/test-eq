
from rest_framework import viewsets
from core import serializers
from core.models import *
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, User. You are at the Core index!")


class BuildingViewSet(viewsets.ModelViewSet):

    queryset = Building.objects.all()
    serializer_class = serializers.BuildingSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.BuildingSerializer
        if self.action == 'retrieve':
            return serializers.BuildingSubSerializer
        return serializers.BuildingSerializer