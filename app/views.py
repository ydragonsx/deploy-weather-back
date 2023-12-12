from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from app.models import FavotiteCity
from app.serializers import FavotiteCitySerializer

class FavotiteCityViewSet(ModelViewSet):
    queryset = FavotiteCity.objects.all()
    serializer_class = FavotiteCitySerializer