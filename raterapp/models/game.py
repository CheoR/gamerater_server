"""Game Model"""
from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=50, blank=False, default="")
    description = models.CharField(max_length=50, blank=False, default="")
    designer = models.CharField(max_length=50, blank=False, default="")
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    play_time = models.IntegerField()
    age_recommendation = models.IntegerField()
