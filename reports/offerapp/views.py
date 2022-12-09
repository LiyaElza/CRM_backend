from django.shortcuts import render
from .serializers import OfferSerializer,SpecialOfferSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from .models import offertable,specialoffer
from crm.models import customers
from reportsapp.models import orders
from django.core import serializers
from django.db import connection
from rest_framework import status
from django.conf import settings
from django.core.mail import send_mail
import jwt
from rest_framework.exceptions import AuthenticationFailed

@api_view(['GET'])
def getroutes(request):
    routes=[
        'aoffer/offer/',
    ]
    return Response(routes)
@api_view(['GET','POST'])
def getoffer(request):
    # token=request.headers['Authorization']

    # if not token:

    #     raise AuthenticationFailed('Unauthenticated')

    # try:

    #     payload=jwt.decode(token,'secret',algorithms=['HS256'])

    # except jwt.ExpiredSignatureError:

    #     raise AuthenticationFailed('Unauthenticated')
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
            mailsend(ptype,subject,product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def mailsend(producttype,subjectsent,product):
    with connection.cursor() as cursor:
        cursor.execute("SELECT crm_customers.Email FROM crm_customers inner join reportsapp_orders on crm_customers.id=reportsapp_orders.customerid_id inner join reportsapp_saleslist on reportsapp_orders.orderid = reportsapp_saleslist.orderid_id  where reportsapp_saleslist.producttype_id= %s",[producttype])
        details=cursor.fetchall()
    recepient_list=[]
    for item in details:
        recepient_list.append(item[0])
    email_from = settings.EMAIL_HOST_USER
    subject=subjectsent
    message="Hii Customers....Please find the offer on your favourite "+product+": "+subjectsent
    send_mail(subject,message, email_from, recepient_list )

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
            mailsend(subject)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def mailsend(subjectsent):
    selcustomers=customers.objects.all()

    recepient_list=[]

    for item in selcustomers:

        customerorderamount=orders.objects.filter(customerid=item.id)

        custamount=0

        for index in customerorderamount:

            custamount=custamount+index.amount

        if(custamount>450):
            recepient_list.append(item.Email)
    email_from = settings.EMAIL_HOST_USER
    subject=subjectsent
    message="Hii Customers....Please find the special offer.."+subjectsent+"Offer valid only for premium customers"
    send_mail(subject,message, email_from, recepient_list )



   