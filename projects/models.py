from django.db import models
from about_me.models import Me
from ckeditor.fields import RichTextField

# Create your models here.
class Project(models.Model):
  me =  models.ForeignKey(Me, on_delete=models.CASCADE)
  name = models.CharField(max_length=200, null=True, blank=True)
  company = models.CharField(max_length=200, null=True, blank=True)
  tools = models.CharField(max_length=200, null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  content = RichTextField(null=True)
  url = models.TextField()
  photo = models.ImageField(upload_to="projects")