from django.db import models
from about_me.models import Me

# Create your models here.
class Project(models.Model):
  me =  models.ForeignKey(Me, on_delete=models.CASCADE)
  name = models.CharField(max_length=200, null=True, blank=True)
  company = models.CharField(max_length=200, null=True, blank=True)
  tools = models.CharField(max_length=200, null=True, blank=True)
  description = models.CharField(max_length=200, null=True, blank=True)
  url = models.TextField()
  photo = models.ImageField(upload_to="projects")