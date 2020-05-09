from django.shortcuts import render
from django.http import JsonResponse

#third party imports
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from app.serializers.artists import ArtistSerializer
from app.models.artist import Artist


class ArtistApiView (generics.ListAPIView):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_fields = ('id',)
