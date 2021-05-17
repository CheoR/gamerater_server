"""Game Image Model"""
from django.db import models


class GameImage(models.Model):
    """GameImage
        User can upload image of the game they are playing.
    """
    gamer = models.OneToOneField("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='images', height_field=None, width_field=None, max_length=None, null=True)
