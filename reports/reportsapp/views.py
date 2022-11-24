from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,FileResponse
from .models import monthlyanalysis,productanalysis
from .serializers import MonthlySalesSerializer,ProductSalesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from io import BytesIO
from reportlab.pdfgen import canvas;


@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/productsales/',
        '/api/monthlysales',
        ]
    return Response(routes)


@api_view(['GET'])
def getmonthlySales(request):
    data_list = monthlyanalysis.objects.all()
    serializer = MonthlySalesSerializer(data_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProductSales(request):
    data_list = productanalysis.objects.all()
    serializer = ProductSalesSerializer(data_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def generateProductReport(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="productreport.pdf"'
    buffer = BytesIO()
    reportText = canvas.Canvas(buffer)
    productReport = productanalysis.objects.all()
    for product in productReport:
        reportText.drawString(400,500,product.producttype)
        reportText.showPage()
    reportText.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

@api_view(['GET'])
def generateMonthlyReport(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="customerreport.pdf"'
    buffer = BytesIO()
    reportText = canvas.Canvas(buffer)
    monthReport = monthlyanalysis.objects.all()
    for month in monthReport:
        reportText.drawString(400,500,month.monthlist)
        reportText.showPage()
    reportText.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
