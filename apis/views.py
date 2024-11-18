from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from apis.models import GeekModels
from apis.serializer import GeeksSerializer

# Create your views here.

class GreekViews(generics.ListAPIView):
    queryset= GeekModels.objects.all()
    serializer_class = GeeksSerializer



