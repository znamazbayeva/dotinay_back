from django.db import models
from about_me.models import Me
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
  me =  models.ForeignKey(Me, on_delete=models.CASCADE)
  title = models.CharField(max_length=200, null=True, blank=True)
  subtitle = models.CharField(max_length=200, null=True, blank=True)
  content = RichTextField()
  photo = models.ImageField()

