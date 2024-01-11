# from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
# from .models import customers
# from .serializers import customersSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
# from django.db import connection
from reportsapp.models import saleslist, orders
from customers.models import customers
from django.forms.models import model_to_dict
from django.core import serializers
from django.db.models import Sum
from django.db.models import Max
import jwt
from rest_framework.exceptions import AuthenticationFailed
from reportsapp.decorators import login_needed

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/home/dashboard/',
       
        ]
    return Response(routes)

#fetching sales details of the organization
# @login_needed
@api_view(['GET'])

def getCounts(request):
    
    
    finalcount=[]
    productquantity=saleslist.objects.values('quantity')
    salescount= 0
    for item in productquantity:
        salescount = salescount + item['quantity']
    finalcount.append(salescount)
    productAmount=orders.objects.values('amount')
    totalincome=0
    for item in productAmount:
        totalincome = totalincome + item['amount']
    finalcount.append(totalincome)
    customerNumber = customers.objects.all().count()
    finalcount.append(customerNumber)
    totalOrders = orders.objects.all().count()
    finalcount.append(totalOrders)
    return Response(finalcount)

