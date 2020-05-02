from rest_framework import serializers

from app.models.show import Representation
from django import forms

class RepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Representation
        fields = '__all__' #all model fields will be included