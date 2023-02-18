from django.urls import re_path
from .consumers.client import player
from .consumers.host import host

websocket_urlpatterns = [
    re_path(r'ws/host/(?P<game_token>\w+)/$', host.HostConsumer),
    re_path(r'ws/join/(?P<game_token>\w+)/$', player.PlayerConsumer),
]