from django.conf.urls import url
from core import serializers

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^buildings/(?P<pk>[0-9]+)/$', serializers.BuildingSerializer.building_details_floor),
]
