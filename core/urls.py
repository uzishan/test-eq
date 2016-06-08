from django.conf.urls import url

from . import views

#urlpatterns = [
#    url(r'^$', views.index, name='index'),

#]
urlpatterns = [
    url(r'^buildings/$', views.building_list),
    url(r'^buildings/(?P<pk>[0-9]+)/$', views.building_detail),
]