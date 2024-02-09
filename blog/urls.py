# views.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from drfblog.models import Blog
from drfblog.serializers import BlogSerializer
from django.shortcuts import get_object_or_404
from django.contrib import admin


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        serializer.save()


# urls.py

router = DefaultRouter()
router.register(r'blogs', BlogViewSet, basename='blog')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
