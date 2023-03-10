from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    tools = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    url = models.TextField()
    photo = models.ImageField(_(""), upload_to="/projects")