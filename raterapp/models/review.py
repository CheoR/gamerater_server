"""Review Model"""
from django.db import models
from django.db.models.deletion import CASCADE


class Review(models.Model):
    """Review model
    """
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    gamer = models.OneToOneField("Gamer", on_delete=CASCADE)
    reivew = models.CharField(max_length=150, blank=True, default="")
    rating = models.IntegerField()
