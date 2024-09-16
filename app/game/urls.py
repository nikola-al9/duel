from django.urls import path
from app.game.apis import *
from app.game.views import *

urlpatterns = [
    path('history/', history_view, name='history'),
    path('backend_history/', GameApi.as_view(), name='backend_history'),
    path('leaderboard/', leaderboard_view, name='leaderboard'),
    path('backend_leaderboard/', LeaderboardApi.as_view(), name='backend_leaderboard'),
]
