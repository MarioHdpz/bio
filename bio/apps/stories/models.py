"""Models definition"""
from colorfield.fields import ColorField
from django.db import models
from positions import PositionField


class Stage(models.Model):
    """Life Stage"""

    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40)
    color = ColorField(default="#FF0000")

    def __str__(self):
        """Set admin label"""
        return self.name


class Story(models.Model):
    """Small story about my life"""

    stage = models.ForeignKey(Stage, on_delete=models.PROTECT)
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=140)
    icon = models.CharField(max_length=20)
    position = PositionField(collection="stage")

    def __str__(self):
        """Set admin name"""
        return self.title
