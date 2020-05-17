from django.shortcuts import render
from django.http import JsonResponse
import requests
import time

#third party imports
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view

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



MAX_RETRIES = 5  # Arbitrary number of times we want to try

@api_view(('GET',))
def external_api_view_test(request):
    if request.method == "GET":
        attempt_num = 0  # keep track of how many times we've retried
        while attempt_num < MAX_RETRIES:
            params = {}
            r = requests.get("https://api.theatredelaville-paris.com/events", timeout=10)
            if r.status_code == 200:
                data = r.json()
                return Response(data, status=status.HTTP_200_OK)
            else:
                attempt_num += 1
                # You can probably use a logger to log the error here
                time.sleep(5)  # Wait for 5 seconds before re-trying
        return Response({"error": "Request failed"}, status=r.status_code)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(('GET',))
def external_api_show_view(request):
    if request.method == "GET":
        attempt_num = 0  # keep track of how many times we've retried
        while attempt_num < MAX_RETRIES:
            dico_data = {}
            r = requests.get("https://api.theatredelaville-paris.com/events", timeout=10)
            if r.status_code == 200:
                for i in range(len(r.json()['hydra:member'])):
                    title = r.json()['hydra:member'][i]['name']
                    slug = r.json()['hydra:member'][i]['slug']
                    #description = r.json()['hydra:member'][i]['seo']['description']
                    description = r.json()['hydra:member'][i]['excerpt']
                    poster = r.json()['hydra:member'][i]['image']
                    bookable = r.json()['hydra:member'][i]['ticketingOpen']
                    price = r.json()['hydra:member'][i]['priceRange']
                    date_created = r.json()['hydra:member'][i]['ticketingOpening']
                    data = {
                        'title' : title,
                        'slug' : slug,
                        'description' : description,
                        'poster' : poster,
                        'bookable' : bookable,
                        'price' : price,
                        'date_created' : date_created,
                        
                    }
                    dico_data["show-" + str(i)] = data
                    
                return Response(dico_data, status=status.HTTP_200_OK)
            else:
                attempt_num += 1
                # You can probably use a logger to log the error here
                time.sleep(5)  # Wait for 5 seconds before re-trying
        return Response({"error": "Request failed"}, status=r.status_code)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)
        
