from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import customers
from .serializers import customersSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
from django.forms.models import model_to_dict
from django.core import serializers




@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/apii/customers/',
      
        ]
    return Response(routes)


@api_view(['GET'])
def getcustomers(request):
    data_list = customers.objects.all()
    serializer = customersSerializer(data_list, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def getcustomerdetails(request):
    customergetid=request.data["id"]
    with connection.cursor() as cursor:
        cursor.execute("SELECT reportsapp_orders.orderid,reportsapp_orders.amount,reportsapp_saleslist.productid_id,projectcrmapp_productstable.title FROM reportsapp_orders inner join reportsapp_saleslist on reportsapp_orders.orderid=reportsapp_saleslist.orderid_id inner join projectcrmapp_productstable on reportsapp_saleslist.productid_id = projectcrmapp_productstable.id  where reportsapp_orders.customerid_id= %s",[customergetid])
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


@api_view(['POST'])
def addCustomer(request):
        if request.method == 'POST' and request.FILES['file']:
            fs=FileSystemStorage()
            filename=fs.save      
            customerexceldata = pd.read_excel(request.FILES['file'] )
            # print(productexceldata)
            dbframe = customerexceldata
            for dbframe in dbframe.itertuples():
                 
                obj = customers.objects.create(id=dbframe.id,FirstName=dbframe.FirstName,
                                                 LastName=dbframe.LastName, Email=dbframe.Email,PhoneNumber=dbframe.PhoneNumber,
                                                joiningDate=dbframe.joiningDate,
                                               )
               
                obj.save()
        return Response({'message':'File Added Successfully'})
