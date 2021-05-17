""" Gamer Model """
from django.contrib.auth.models import User
from django.db import models


class Gamer(models.Model):
    """Gamer model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50, blank=True, default="")

    def __str__(self):
        return str(self.user.username)
