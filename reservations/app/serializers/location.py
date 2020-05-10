from rest_framework import serializers

from app.models.location import Location
from django import forms

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__' #all model fields will be included