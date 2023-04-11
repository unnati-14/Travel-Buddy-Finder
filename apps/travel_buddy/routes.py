# from django.conf.urls import url
from django.urls import re_path, include

from . import views

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^register$', views.register),
    re_path(r'^login$', views.login),
    re_path(r'^travel$', views.travel),
    re_path(r'^addplan$', views.addplan),
    re_path(r'^createplan$', views.createplan),
    re_path(r'^show/(?P<travel_id>\d+)$', views.show),
    re_path(r'^join/(?P<travel_id>\d+)$', views.join),
    re_path(r'^logout$', views.logout),
    re_path(r'^delete/(?P<id>\d+)$', views.delete)
]
