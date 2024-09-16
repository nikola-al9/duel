from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app.game.selectors import GameSelector

class GameApi(APIView):
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        res = GameSelector(
            user=request.user,
            query_params=request.query_params.copy()
        ).list_history_games()
        return Response(res)


class LeaderboardApi(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        res = GameSelector(
            user=request.user,
            query_params=request.query_params.copy()
        ).leaderboard()
        return Response(res)
