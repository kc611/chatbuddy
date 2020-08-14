from django.urls import re_path

from . import users

websocket_urlpatterns = [
    re_path(r'ws/(?P<room_name>\w+)/$', users.ChatUser),
]