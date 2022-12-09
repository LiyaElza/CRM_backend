from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,FileResponse,HttpRequest
from .models import monthlyanalysis,productanalysis,orders
from crm.models import customers
from crm.serializers import customersSerializer
from .serializers import MonthlySalesSerializer,ProductSalesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from io import BytesIO
from datetime import date
from .utils import html_to_pdf
from django.views.generic import View
from django.template.loader import render_to_string
from django.urls import reverse
import jwt
from rest_framework.exceptions import AuthenticationFailed


@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/productsales/',
        '/api/monthlysales',
        ]
    return Response(routes)


@api_view(['GET'])
def getmonthlySales(request):
    # token=request.headers['Authorization']

    # if not token:

    #     raise AuthenticationFailed('Unauthenticated')

    # try:

    #     payload=jwt.decode(token,'secret',algorithms=['HS256'])

    # except jwt.ExpiredSignatureError:

    #     raise AuthenticationFailed('Unauthenticated')
    data_list = monthlyanalysis.objects.all()
    serializer = MonthlySalesSerializer(data_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProductSales(request):
    # token=request.headers['Authorization']

    # if not token:

    #     raise AuthenticationFailed('Unauthenticated')

    # try:

    #     payload=jwt.decode(token,'secret',algorithms=['HS256'])

    # except jwt.ExpiredSignatureError:

    #     raise AuthenticationFailed('Unauthenticated')
    data_list = productanalysis.objects.all()
    serializer = ProductSalesSerializer(data_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def CustomerGrowth(request):
    # token=request.headers['Authorization']

    # if not token:

    #     raise AuthenticationFailed('Unauthenticated')

    # try:

    #     payload=jwt.decode(token,'secret',algorithms=['HS256'])

    # except jwt.ExpiredSignatureError:

    #     raise AuthenticationFailed('Unauthenticated')
    data_list = customers.objects.all()
    export_list=[]
    data_items={}
    for item in data_list:
        datem = item.joiningDate.strftime("%Y")
        if datem in data_items:
            data_items[datem]+=1
        else:
            data_items[datem]=1
    for key,item in data_items.items():
        item={"year":key,"number":item}
        export_list.append(item)
    return Response(export_list)

class generateCustomerReport(View):
     def get(self, request, *args, **kwargs):
        data_list = customers.objects.all()
        export_list=[]
        data_items={}
        for item in data_list:
            datem = item.joiningDate.strftime("%Y")
            if datem in data_items:
                data_items[datem]+=1
            else:
                data_items[datem]=1
        for key,item in data_items.items():
            item={"year":key,"number":item}
            export_list.append(item)
        open('templates/temp.html', "w").write(render_to_string('customerreport.html', {'data': export_list}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

class generateProductReport(View):
     def get(self, request, *args, **kwargs):
        data = productanalysis.objects.all()
        open('templates/temp.html', "w").write(render_to_string('productreport.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

class generateMonthlyReport(View):
     def get(self, request, *args, **kwargs):
        data = monthlyanalysis.objects.all()
        open('templates/temp.html', "w").write(render_to_string('monthlyreport.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')


