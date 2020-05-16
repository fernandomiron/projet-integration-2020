from rest_framework import serializers

from app.models.show import Show


class ShowSerializer(serializers.ModelSerializer):
    """Generic model serializer on Show."""

    class Meta:
        """Meta definition for serializer."""

        model = Show
        fields = '__all__'
