from rest_framework import serializers

from app.models.artist import ArtistType,Types,Artist
from django import forms

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__' #all model fields will be included
        
