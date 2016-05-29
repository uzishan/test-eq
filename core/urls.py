from django.conf.urls import url
from core import views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^buildings/(?P<pk>[0-9]+)/$', views.FloorViewSet),
]
