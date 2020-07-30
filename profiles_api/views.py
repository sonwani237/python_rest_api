from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


# Create your views here.

class HelloApiView(APIView):
    """Test API View"""
    serializers_class = serializers.HelloSerializer

    def get(self, request, formate=None):
        """Returen a list of APIView features"""
        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar, to a trasitional Django view',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Success', 'an_apiview': an_apiview})

    def post(self, request):
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """"Handel updating request"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """"Handel updating request"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """"Handel updating request"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """"Test Api ViewSet"""

    serializers_class = serializers.HelloSerializer

    def list(self, request):
        """"Return a hello message"""
        a_viewset = [
            'User action (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'method': 'GET'})

    def update(self, request, pk=None):
        """Handle update an object"""
        return Response({'method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle partial update an object """
        return Response({'method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle delete an object"""
        return Response({'method': 'DELETE'})
