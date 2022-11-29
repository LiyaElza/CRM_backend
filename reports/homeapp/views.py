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
from reportsapp.models import saleslist, orders, customers
from django.forms.models import model_to_dict
from django.core import serializers
from django.db.models import Sum
from django.db.models import Max

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api2/quantity/',
        '/api2/income/',
        '/api2/customerno/',
        '/api2/totalorders/',
        ]
    return Response(routes)

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

# @api_view(['GET'])
# def getIncome(request):
#     productAmount=orders.objects.values('amount')
#     amount=0
#     for item in productAmount:
#         amount = amount + item['amount']
#     return Response(amount)


# @api_view(['GET'])
# def getCustomerNumber(request):
#     customerNumber = customers.objects.aggregate(Max('id')).get('id__max')
#     return Response(customerNumber)


# @api_view(['GET'])
# def getTotalOrders(request):
#     totalOrders = orders.objects.all().count()
#     return Response(totalOrders)
