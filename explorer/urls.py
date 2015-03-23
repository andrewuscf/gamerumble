from django.conf.urls import *

from explorer import views

urlpatterns = patterns('',
    url(r'^$', views.explorer, name='explorer-home'),
    url(r'^players/$', views.get_player_names, name='players'),
)