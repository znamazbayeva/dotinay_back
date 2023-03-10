from django.db import models

# Create your models here.
class Me(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    occupation = models.CharField(max_length=200, null=True, blank=True)
    intro = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField()

