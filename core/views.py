
from rest_framework import viewsets
from core.serializers import *
from core.models import *
from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


def index(request):
    return HttpResponse("Hello, User. You are at the Core index!")


class BuildingViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Building.objects.all()
        serializer = BuildingSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Building.objects.all()
        building = get_object_or_404(queryset, pk=pk)
        serializer = BuildingSubSerializer(building)
        return Response(serializer.data)