from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import generics
from rest_framework.permissions import (
    AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.views import APIView
from url_filter.integrations.drf import DjangoFilterBackend

from app.models.artist import Artist
from app.models.location import Location
from app.models.show import Representation
from app.models.show import Show
from app.serializers.artists import ArtistSerializer
from app.serializers.location import LocationSerializer
from app.serializers.representation import RepresentationSerializer
from app.serializers.show import ShowSerializer


class ArtistApiView (generics.ListAPIView):
    """ Comment here """  # TODO: Comment class

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('id', 'lastname')


class RepresentationApiView (generics.ListAPIView):
    """ Comment here """  # TODO: Comment class

    queryset = Representation.objects.all()
    serializer_class = RepresentationSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('id', 'location')


class ShowApiView (generics.ListAPIView):
    """ Comment here """  # TODO: Comment class

    queryset = Show.objects.all()
    serializer_class = ShowSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('id', 'title')


class LocationApiView (generics.ListAPIView):
    """ Comment here """  # TODO: Comment class

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('id', 'designation')
