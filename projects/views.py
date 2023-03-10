from django.shortcuts import render
from .serializers import ProjectSerializer
from .models import Project
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ProjectSerializer
    parser_classes = [(MultiPartParser)]
    queryset = Project.objects.all()

