from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MailModel
from .serializers import mailSerializer
from crm.models import customers
from rest_framework import status


# def sendemails(request):
#     email="achuaswanth185@gmail.com"
#     subject = 'welcome to PyCo CRM'
#     message = f'Hi, thank you for registering with PyCo CRM.'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [email, ]
#     send_mail(subject,message, email_from, recipient_list )
#     return render(request,"index.html")
# # Create your views here.

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
        return Response(request.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
