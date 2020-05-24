from django.shortcuts import render
from django.http import JsonResponse
import requests
import time

#third party imports
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework import generics, viewsets, status
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

class ExternalAPIShowView(generics.GenericAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
    # Get the list of show from Théatre de la ville de Paris
    def get(self, request, *args, **kwargs):
        data_list = []
        attempt_num = 0  # keep track of how many times we've retried
        external_api_url = "https://api.theatredelaville-paris.com/events" 
        r = requests.get(external_api_url, timeout=10)
        data_all = r.json()
        while attempt_num < MAX_RETRIES:
            if r.status_code == 200:
                for i in range(len(data_all['hydra:member'])):
                    title = data_all['hydra:member'][i]['name']
                    #slug = data_all['hydra:member'][i]['slug']
                    description = data_all['hydra:member'][i]['excerpt']
                    bookable = data_all['hydra:member'][i]['ticketingOpen']
                    price = str(data_all['hydra:member'][i]['priceRange'])
                    date_created = data_all['hydra:member'][i]['ticketingOpening']
                    image = data_all['hydra:member'][i]['image']

                    if image != None : 
                        poster = image['contentUrl']['medium']

                    # Extract the price from the string 
                    if price == 'None':
                        price = 0
                    elif price[0] == 'd' or price[0] == 'D':
                        price = price[3:5].strip()
                    else :
                        price = price[:2]
                        if price[1] == '€':
                            price = price[0]
                        else:
                            price = price.strip()
                    
                    #Convert the price in Integer
                    price = int(price)

                    data_filtered = {
                        'title' : title,
                        #'slug' : slug,
                        'description' : description,
                        'poster' : poster,
                        'bookable' : bookable,
                        'price' : price,
                        'date_created' : date_created,
                    }
                    data_list.append(data_filtered) 
                return Response(data_list, status=status.HTTP_200_OK)
            else:
                    attempt_num += 1
                    time.sleep(5)  # Wait for 5 seconds before re-trying
            return Response({"error": "Request failed"}, status=r.status_code)
    


class ExternalAPI(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        attempt_num = 0  # keep track of how many times we've retried
        external_api_url = "http://127.0.0.1:8000/external-api/show/" 
        r = requests.get(external_api_url, timeout=10)
        data_all = r.json()
        while attempt_num < MAX_RETRIES:
            if r.status_code == 200:
                data = data_all
                return Response(data, status=status.HTTP_200_OK)
            else:
                    attempt_num += 1
                    time.sleep(5)  # Wait for 5 seconds before re-trying
            return Response({"error": "Request failed"}, status=r.status_code)



from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
def api_detail_show_view(request, slug):
    
    try:
        show = Show.objects.get(slug=slug)
    except Show.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ShowSerializer(show)
        return Response(serializer.data)

@api_view(['PUT'])
def api_update_show_view(request, slug):
    
    try:
        show = Show.objects.get(slug=slug)
    except Show.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = ShowSerializer(show, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_delele_show_view(request, slug):
    
    try:
        show = Show.objects.get(slug=slug)
    except Show.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        operation = show.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)

@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def api_create_show_view(request):
    
    if request.method == 'POST':
        serializer = ShowSerializer(Show(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


