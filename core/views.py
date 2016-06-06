from django.shortcuts import render
from rest_framework import viewsets
from core.serializers import BuildingSerializer, BuildingSubSerializer
from core.models import *
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, User. You are at the Core index!")


class BuildingViewSet(viewsets.ModelViewSet):

    queryset = Building.objects.all().order_by('pk')
    serializer_class = BuildingSerializer


class BuildingSubViewSet(viewsets.ModelViewSet):

    queryset = Building.objects.all().order_by('pk')
    serializer_class = BuildingSubSerializer
