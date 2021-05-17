"""Category Model"""
from django.db import models


class Category(models.Model):
    """Category Model
    """
    label = models.CharField(max_length=50, blank=False, default="")

    def __str__(self):
        return str(self.label)
