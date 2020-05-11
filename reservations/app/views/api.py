from django.shortcuts import render
from django.http import JsonResponse

#third party imports
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

#don't forget adding url_filter in settings
from url_filter.integrations.drf import DjangoFilterBackend

#information import about Artist
from app.serializers.artists import ArtistSerializer
from app.models.artist import Artist

#informations import about show
from app.serializers.show import ShowSerializer
from app.models.show import Show

#informations import about Representation
from app.serializers.representation import RepresentationSerializer
from app.models.show import Representation

#informations import about Location
from app.serializers.location import LocationSerializer
from app.models.location import Location


class ArtistApiView (generics.ListAPIView):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('id','lastname')

class RepresentationApiView (generics.ListAPIView):
    queryset = Representation.objects.all()
    serializer_class = RepresentationSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('id', 'location')


class ShowApiView (generics.ListAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('id', 'title')

class LocationApiView (generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('id', 'designation')