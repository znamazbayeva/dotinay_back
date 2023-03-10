from django.shortcuts import render
from .serializers import MeSerializer
from .models import Me
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
# Create your views here.

class MeViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = MeSerializer
    parser_classes = [(MultiPartParser)]
    queryset = Me.objects.all()
