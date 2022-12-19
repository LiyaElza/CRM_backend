from django.shortcuts import render
from rest_framework import status

# Create your views here.
from .serializers import HeroSerializer
from .models import productstable
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from .models import productstable
from django.core import serializers
import pandas as pd
from django.core.files.storage import FileSystemStorage
import os
import jwt
from rest_framework.exceptions import AuthenticationFailed

@api_view(['GET'])
def getroutes(request):
    routes=[
        'products/products/',
        
    ]
    return Response(routes)


#displaying products
@api_view(['GET','POST'])
def getproducts(request):
    data_list = productstable.objects.all()
    if request.method == 'GET':
        serializer = HeroSerializer(data_list, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#reading from csv files
@api_view(['POST'])
def Import_csv(request):
    if request.method == 'POST' and request.FILES['file']:
        fs=FileSystemStorage()
        filename=fs.save      
        productexceldata = pd.read_excel(request.FILES['file'] )
        dbframe = productexceldata
        for dbframe in dbframe.itertuples():
                 
            obj = productstable.objects.create(id=dbframe.id,title=dbframe.title,
                                                 category=dbframe.category, thiruvalla=dbframe.thiruvalla, kottayam=dbframe.kottayam,
                                                kochi=dbframe.kochi, img=dbframe.img,
                                               )
               
            obj.save()
        return Response({'message':'File Added Successfully'})
