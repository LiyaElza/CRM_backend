from django.shortcuts import render
from django.http import JsonResponse
from .models import customers
from .serializers import customersSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers

@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/apii/customers/',
      
        ]
    return Response(routes)


@api_view(['GET'])
def getcustomers(request):
    data_list = customers.objects.all()
    serializer = customersSerializer(data_list, many=True)
    return Response(serializer.data)

# Create your views here.
