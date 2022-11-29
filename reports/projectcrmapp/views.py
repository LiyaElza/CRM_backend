from django.shortcuts import render
from rest_framework import status

# Create your views here.
from .serializers import HeroSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
# from .products import products
# from .meals import meals
from .models import productstable
from django.core import serializers



@api_view(['GET'])
def getroutes(request):
    routes=[
        'api/products/',
        
    ]
    return Response(routes)



@api_view(['GET','POST'])
def getproducts(request):
    data_list = productstable.objects.all()
    if request.method == 'GET':
        serializer = HeroSerializer(data_list, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = HeroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)