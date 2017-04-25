from .models import Place
from rest_framework import serializers


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ("id", "name", "description", "address",
                  "phone_number", "url", "position_lat", "position_lng", "category")
