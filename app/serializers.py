from rest_framework.serializers import ModelSerializer

from app.models import FavotiteCity

class FavotiteCitySerializer(ModelSerializer):
    class Meta:
        model = FavotiteCity
        fields = "__all__"