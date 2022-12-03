from django.shortcuts import render
from rest_framework import status

# Create your views here.
from .serializers import HeroSerializer
from projectcrmapp.models import productstable
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
# from .products import products
# from .meals import meals
from .models import productstable
from django.core import serializers
import pandas as pd
from django.core.files.storage import FileSystemStorage
import os

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
    # elif request.method == 'POST':
    #     serializer = HeroSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def Import_csv(request):
        if request.method == 'POST' and request.FILES['file']:
            fs=FileSystemStorage()
            filename=fs.save      
            productexceldata = pd.read_excel(request.FILES['file'] )
            # print(productexceldata)
            dbframe = productexceldata
            for dbframe in dbframe.itertuples():
                 
                obj = productstable.objects.create(id=dbframe.id,title=dbframe.title,
                                                 category=dbframe.category, thiruvalla=dbframe.thiruvalla, kottayam=dbframe.kottayam,
                                                kochi=dbframe.kochi, img=dbframe.img,
                                               )
               
                obj.save()
        return Response({'message':'File Added Successfully'})
