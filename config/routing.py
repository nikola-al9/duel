from django.urls import path
from app.game.consumers import GameConsumer

websocket_urlpatterns = [
    path('ws/play/', GameConsumer.as_asgi()),
]