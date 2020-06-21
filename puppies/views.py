from .models import Puppy
from .serializers import PuppySerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated



class PuppyList(APIView):
    """
    Authenticated user should get all puppies, or create a new puppy.
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PuppySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PuppyDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = (IsAuthenticated,)
    
    def get_object(self, pk):
        try:
            return Puppy.objects.get(pk=pk)
        except Puppy.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        puppy = self.get_object(pk)
        serializer = PuppySerializer(puppy)
        return Response(serializer.data)

    def put(self, request, pk):
        puppy = self.get_object(pk)
        serializer = PuppySerializer(puppy, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        puppy = self.get_object(pk)
        puppy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
