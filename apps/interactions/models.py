from django.db import models
from django.contrib.auth.models import User
from apps.games.models import Game

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(default=5)  # Valoración 1-5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reseña de {self.user} para {self.game}'

class Like(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Like de {self.user} en {self.game}'
