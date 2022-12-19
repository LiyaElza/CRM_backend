from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MailModel
from .serializers import mailSerializer
from customers.models import customers
from rest_framework import status
import jwt
from rest_framework.exceptions import AuthenticationFailed

#send mails to customers
@api_view(['POST'])
def sendemails(request):
    subject=request.data["subject"]
    message=request.data["message"]
    email_from = settings.EMAIL_HOST_USER
    recepients=customers.objects.values_list('Email')
    recepient_list=[]
    for item in recepients:
        recepient_list.append(item[0])
    send_mail(subject,message, email_from, recepient_list )
    serializer = mailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message="Message Sent"
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
