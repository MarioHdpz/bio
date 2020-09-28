"""Models definition"""
from django.db import models
from positions import PositionField


class Stage(models.Model):
    """Life Stage"""

    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40)
    image = models.ImageField(upload_to="stages", null=True)
    position = PositionField()

    def __str__(self):
        """Set admin label"""
        return self.name

    class Meta:
        """Set verbose names"""

        verbose_name = "Stage"
        verbose_name_plural = "Stages"


class Story(models.Model):
    """Small story about my life"""

    stage = models.ForeignKey(Stage, on_delete=models.PROTECT)
    title = models.CharField(max_length=20)
    text = models.TextField(max_length=280)
    icon = models.ImageField(upload_to="story-icons", null=True)
    date = models.DateField()

    def __str__(self):
        """Set admin name"""
        return self.title

    class Meta:
        """Set verbose names"""

        verbose_name = "Story"
        verbose_name_plural = "Stories"
