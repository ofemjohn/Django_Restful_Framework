from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer
from django.shortcuts import get_object_or_404


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        serializer.save()
