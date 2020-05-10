from rest_framework import serializers

from app.models.show import Show
from django import forms

class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = '__all__' #all model fields will be included