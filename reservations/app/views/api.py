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

#informations import about Representation
from app.serializers.representation import RepresentationSerializer
from app.models.show import Representation

class ArtistApiView (generics.ListAPIView):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('id','lastname')

class representationApiView (generics.ListAPIView):
    queryset = Representation.objects.all()
    serializer_class = RepresentationSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('id', 'location')