from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData

class MovieViewSet(viewsets.ModelViewSet):
  queryset = MovieData.objects.all()
  serializer_class = MovieSerializer

