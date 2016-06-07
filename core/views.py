
from rest_framework import viewsets
from core import serializers
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, User. You are at the Core index!")


class BuildingViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.BuildingSerializer
        if self.action == 'retrieve':
            return serializers.BuildingSubSerializer
