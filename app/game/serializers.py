from rest_framework import serializers
from app.users.serializers import BasicAccountInfoSerializer
from app.game.models import Game

class GameSerializer(serializers.ModelSerializer):
    win_or_loss = serializers.SerializerMethodField()
    player = serializers.SerializerMethodField()
    class Meta:
        model = Game
        fields = [
            'id',
            'created_at',
            'closed_at',
            'player',
            'win_or_loss'
        ]

    def get_win_or_loss(self, obj):
        if obj.winner_id == self.context['user'].id:
            return 'win'
        return 'loss'

    def get_player(self, obj):
        if obj.player_1_id == self.context['user'].id:
            return BasicAccountInfoSerializer(obj.player_2).data
        return BasicAccountInfoSerializer(obj.player_1).data