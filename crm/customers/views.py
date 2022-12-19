import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import customers
from reportsapp.models import orders
from .serializers import customersSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
from django.forms.models import model_to_dict
from django.core import serializers
import jwt
from rest_framework.exceptions import AuthenticationFailed
from reportsapp.decorators import login_needed

@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/apii/customers/',
      
        ]
    return Response(routes)

#get details of customers
@login_needed
@api_view(['GET'])
def getcustomers(request):
    data_list = customers.objects.all()
    serializer = customersSerializer(data_list, many=True)
    return Response(serializer.data)

#get order details of customers by fetching details from orders and saleslist
@api_view(['POST'])
def getcustomerdetails(request):
    customergetid=request.data["id"]
    with connection.cursor() as cursor:
        cursor.execute("SELECT reportsapp_orders.orderid,reportsapp_orders.amount,reportsapp_saleslist.productid_id,products_productstable.title FROM reportsapp_orders inner join reportsapp_saleslist on reportsapp_orders.orderid=reportsapp_saleslist.orderid_id inner join products_productstable on reportsapp_saleslist.productid_id = products_productstable.id  where reportsapp_orders.customerid_id= %s",[customergetid])
        details=cursor.fetchall()
    final_list=[]
    for item in details:
        singleitem={}
        singleitem["orderId"]=item[0]
        singleitem["Amount"]=item[1]
        singleitem["ProductId"]=item[2]
        singleitem["ProductName"]=item[3]
        final_list.append(singleitem)
    return Response(final_list)

#adding customer bulk data via excel sheet upload
@api_view(['POST'])
def addCustomer(request):
        if request.method == 'POST' and request.FILES['file']:
            fs=FileSystemStorage()
            filename=fs.save      
            customerexceldata = pd.read_excel(request.FILES['file'] )
            dbframe = customerexceldata
            for dbframe in dbframe.itertuples():
                 
                obj = customers.objects.create(id=dbframe.id,FirstName=dbframe.FirstName,
                                                 LastName=dbframe.LastName, Email=dbframe.Email,PhoneNumber=dbframe.PhoneNumber,
                                                joiningDate=dbframe.joiningDate,
                                               )
               
                obj.save()
        return Response({'message':'File Added Successfully'})

#displaying customers with most credits as premium customers
@api_view(['GET'])

def plusCustomers(request):

    selcustomers=customers.objects.all()

    finallist=[]

    for item in selcustomers:

        customerorderamount=orders.objects.filter(customerid=item.id)
        frequency=0
        custamount=0
        credit=0

        for index in customerorderamount:
            frequency+=1
            custamount=custamount+index.amount
            
        credits=custamount//100
        if(frequency>=2):
            credit+=(frequency//2)
        if(credits>6):
            data_list = customers.objects.get(pk=item.id)
            serializer = customersSerializer(instance=data_list, data={"premium":1,"credits":credits}, partial=True)
            if serializer.is_valid():
                serializer.save()
            finallist.append({"id":item.id,"FirstName":item.FirstName,"LastName":item.LastName,"Email":item.Email,"phone":item.PhoneNumber,"credits":credits})
        else:
            data_list = customers.objects.get(pk=item.id)
            serializer = customersSerializer(instance=data_list, data={"premium":0,"credits":credits}, partial=True)
            if serializer.is_valid():
                serializer.save()

    return Response(finallist)
