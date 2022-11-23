from django.shortcuts import render
from django.http import JsonResponse
from .models import monthlyanalysis
from .serializers import MonthlySalesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers

@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/products/',
        '/api/monthlysales',
        ]
    return Response(routes)


@api_view(['GET'])
def getmonthlySales(request):
    data_list = monthlyanalysis.objects.all()
    serializer = MonthlySalesSerializer(data_list, many=True)
    return Response(serializer.data)




# Create your views here.

