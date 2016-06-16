from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^new', views.new, name='new'),
  url(r'^create', views.create, name='create'),
  url(r'^show/(?P<id>[0-9A-Za-z]+)/$', views.show, name='new'),
]
