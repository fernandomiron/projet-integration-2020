from rest_framework import serializers

from models.artist import *
from django import forms

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = {
            'firstname', 'lastname'
        }
