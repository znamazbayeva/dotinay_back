from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Me(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    occupation = models.CharField(max_length=200, null=True, blank=True)
    intro = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField()
    content = RichTextField(null=True)

