from django.urls import path, re_path
from . import views

app_name = 'buddy'
urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?P<poo>[^$]+)/(?P<var>[0-9]+)$', views.detail, name='detail'),
    re_path(r'^(?P<var>[0-9]+)/favorites$', views.favorites, name='favorites'),
]
