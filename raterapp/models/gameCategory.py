"""Game Category Model"""
from django.db import models


class GameCategory(models.Model):
    """Game Category
    """
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    category = models.CharField(max_length=20, blank=False, default="")

    def __str__(self):
        return f"{self.game} has categor of {self.category}"
