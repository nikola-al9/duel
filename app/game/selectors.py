from app.common.selectors import SelectorAbstract
from app.common.utils import get_response
from app.game.serializers import *
from django.db.models import Q
from app.users.models import Account
from app.users.serializers import BasicAccountInfoSerializer

class GameSelector(SelectorAbstract):
    def list_history_games(self):
        limit = 50

        games = Game.objects.filter(
            Q(player_1=self.user) | Q(player_2=self.user)
        ).order_by('-created_at')[:limit]

        context = {'user': self.user}
        res = GameSerializer(games, many=True, context=context).data
        return get_response(res)

    def leaderboard(self):
        limit = 50

        players = Account.objects.all().order_by('-points')[:limit]
        res = BasicAccountInfoSerializer(players, many=True).data
        return get_response(res)
