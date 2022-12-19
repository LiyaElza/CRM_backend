from django.shortcuts import render
from .models import User
from django.contrib.auth import authenticate
from .serializers import userSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from rest_framework.response import Response
import jwt,datetime

# Create your views here.
@api_view(['post'])
def register(request):
    serializer = userSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

#login using JWT
@api_view(['POST'])
def login(request):
    email=request.data['email']
    password=request.data['password']
    user=User.objects.filter(email=email).first()
    # print("id=",user.id)
    if user is None:
        raise AuthenticationFailed('user not found')
    if not user.password == password:
        raise AuthenticationFailed('inncorrect password')
    payload={
        'id':user.id,
        'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
        'iat':datetime.datetime.utcnow()
        }
    token=jwt.encode(payload,'secret',algorithm='HS256')
    response=Response()
    response.set_cookie(key='jwt',value=token,httponly=True)
    response.data={
        'jwt':token,'username':user.email
    }
    return response

#logout
@api_view(['POST'])
def logout(request):
    response=Response()
    response.delete_cookie('jwt')
    response.data={
        'message':'sucess'
    }
    return response