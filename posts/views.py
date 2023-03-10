from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PostSerializer
    parser_classes = [(MultiPartParser)]
    queryset = Post.objects.all()

