from django.shortcuts import render
from django.http import JsonResponse

#third party imports
from rest_framework.views import APIView
from rest_framework.response import Response

from app.serializers.artists import ArtistSerializer
from app.models.artist import Artist,ArtistType,Types

class ApiGetView (APIView) :
    def get(self, request, *args, **kwargs):
        qsArtist = Artist.objects.all()
        serializer = ArtistSerializer(qsArtist, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response(serializer.errors)


