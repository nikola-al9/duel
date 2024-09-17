from django.urls import re_path
from app.game import consumers

websocket_urlpatterns = [
    re_path(r'ws/game/(?P<room_name>\w+)/$', consumers.GameConsumer.as_asgi()),
]
