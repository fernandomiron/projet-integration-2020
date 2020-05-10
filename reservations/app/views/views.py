from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.serializers import serializers 


class APINameView(APIView):
    # Test API View

    # Specify wich serializers is used
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        # Returns a list of APIView features

        api_view = [
            "Uses HTTP methods as function(get, post, patch, put, delete)",
            "It's similar to traditional Django view",
            "Is mapped manually to URLs"
        ]

        return Response({'message' : 'Hello!', 'api_view' : api_view})

    def post(self, request):
        # Create a hello message with our name

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        # Handles updating an object

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        # Patch request, only updates fields provided in the request

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        # Delete an object

        return Response({'method': 'delete'})








def home(request):
    """Default test homepage with base-template"""

    return render(request, 'app/base.html', {})
    
