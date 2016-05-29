from django.shortcuts import render
from rest_framework import viewsets
from core.serializers import BuildingSerializer, FloorSerializer
from core.models import *
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, User. You are at the Core index!")


class BuildingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Buildings to be viewed or edited.
    """
    queryset = Building.objects.all().order_by('pk')
    serializer_class = BuildingSerializer

class FloorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Floors to be viewed or edited.
    """
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
