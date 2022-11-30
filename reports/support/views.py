from django.shortcuts import render
from .models import supportlist
from .serializers import SupporListSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def getsupport(request):
    data_list = supportlist.objects.all()
    if request.method == 'GET':
        serializer = SupporListSerializer(data_list, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SupporListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT','DELETE'])  
def editSupport(request,pk):
    data_list = supportlist.objects.get(pk=pk)
    if request.method == 'PUT':
        serializer = SupporListSerializer(instance=data_list, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)