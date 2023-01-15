from django.http import JsonResponse
from .models import BigBuisness
from .serializers import DeltaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def business_list(request, format=None):
    if request.method == 'GET':
        #Get names of all small businesses
        businesses = BigBuisness.objects.all()

        #Serialize them
        serializer = DeltaSerializer(businesses, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DeltaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def business_detail(request, id, format=None):

    try:
        business = BigBuisness.objects.get(pk=id)
    except BigBuisness.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DeltaSerializer(business)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DeltaSerializer(business, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        business.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
