from django.db import models

class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(blank=True, null=True, default=None)
    player_1 = models.ForeignKey('users.Account', on_delete=models.CASCADE, related_name='player_1')
    player_2 = models.ForeignKey('users.Account', on_delete=models.CASCADE, related_name='player_2')
    winner = models.ForeignKey('users.Account', on_delete=models.CASCADE, related_name='game_wins', blank=True, null=True, default=None)
