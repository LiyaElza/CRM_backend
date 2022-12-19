from django.shortcuts import render
from .serializers import OfferSerializer,SpecialOfferSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from .models import offertable,specialoffer
from customers.models import customers
from reportsapp.models import orders
from django.core import serializers
from django.db import connection
from rest_framework import status
from django.conf import settings
from django.core.mail import send_mail
import jwt
from rest_framework.exceptions import AuthenticationFailed
from reportsapp.decorators import login_needed

@api_view(['GET'])
def getroutes(request):
    routes=[
        'aoffer/offer/',
    ]
    return Response(routes)
    

@api_view(['GET','POST'])

#adding and displaying offers
def getoffer(request):
    if request.method == 'GET':
        data_list = offertable.objects.all()
        serializer = OfferSerializer(data_list, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            ptype=serializer.data['product_type']
            product=serializer.data['product']
            subject=serializer.data['message']
            startdate=serializer.data['startDate']
            enddate=serializer.data['endDate']
            mailsend(ptype,subject,product,startdate,enddate)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#function for mailing based on producttype
def mailsend(producttype,subjectsent,product,startdate,enddate):
    with connection.cursor() as cursor:
        cursor.execute("SELECT customers_customers.Email FROM customers_customers inner join reportsapp_orders on customers_customers.id=reportsapp_orders.customerid_id inner join reportsapp_saleslist on reportsapp_orders.orderid = reportsapp_saleslist.orderid_id  where reportsapp_saleslist.producttype_id= %s",[producttype])
        details=cursor.fetchall()
    recepient_list=[]
    for item in details:
        recepient_list.append(item[0])
    email_from = settings.EMAIL_HOST_USER
    subject=subjectsent
    message="Hii Customers....Please find the offer on your favourite "+product+": "+subjectsent+"The offer is valid from "+startdate+"to "+enddate
    send_mail(subject,message, email_from, recepient_list )

#adding offers for selected customers
@api_view(['GET','POST'])
def getspecialoffer(request):
    if request.method == 'GET':
        data_list = specialoffer.objects.all()
        serializer = SpecialOfferSerializer(data_list, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SpecialOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            subject=serializer.data['offer']
            startdate=serializer.data['startDate']
            enddate=serializer.data['endDate']
            mincredits=serializer.data['minCredits']
            mailsendSP(subject,startdate,enddate,mincredits)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#mailing offers to premium customers
def mailsendSP(subjectsent,startdate,enddate,mincredits):
    selcustomers=customers.objects.all()

    recepient_list=[]

    for item in selcustomers:
        if(item.credits>mincredits):
            recepient_list.append(item.Email)
    email_from = settings.EMAIL_HOST_USER
    subject=subjectsent
    message="Hii Customers....Please find the special offer.."+subjectsent+"Offer valid only for premium customers"+"The offer is valid from "+startdate+"to "+enddate
    send_mail(subject,message, email_from, recepient_list )

