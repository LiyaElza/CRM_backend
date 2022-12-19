from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from itertools import combinations
from collections import Counter
import pymysql
from os import environ
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from django.http import HttpResponse,FileResponse
from datetime import datetime

@api_view(['GET'])
def getroutes(request):
    routes=[
        'analysis/',
        
    ]
    return Response(routes)


#evaluating hourly sales in the store based on quantity
@api_view(['GET'])
def getadrecommendation(request):

    
    engine = create_engine("mysql+pymysql://root:%s@localhost:3306/project" % quote_plus("liya@1264"))
    all_data = pd.read_sql_table("analysis_data",con=engine)
    all_data=all_data.dropna(how='all')
    all_data['Order_Date_DTO']=pd.to_datetime(all_data['Order Date'],errors='coerce')
    all_data['Hour']=all_data['Order_Date_DTO'].dt.hour
    all_data.head()
    resultsnew=all_data.groupby(['Hour'])['Quantity Ordered'].count()
    return Response(resultsnew)

#getting most sold products as bundles
@api_view(['GET'])
def getproductbundles(request):

    engine = create_engine("mysql+pymysql://root:%s@localhost:3306/project" % quote_plus("liya@1264"))
    all_data = pd.read_sql_table("analysis_data",con=engine)
    all_data=all_data.dropna(how='all')
    new_all = all_data[all_data['Order ID'].duplicated(keep=False)]
    new_all['Product_Bundle']=new_all.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
    new_all = new_all[['Order ID','Product_Bundle']].drop_duplicates()
    new_all.head()
    count=Counter()

    for row in new_all['Product_Bundle']:
        row_list=row.split(',')
        count.update(Counter(combinations(row_list,3)))

    count=count.most_common(20)
    for item in count:
        results = dict((x, y) for x, y in count)
        results = {", ".join(key): value for key, value in results.items()}
    return Response(results)



#getting products in an every hour
@api_view(['GET'])
def gethourlyproductanalysis(request):

    engine = create_engine("mysql+pymysql://root:%s@localhost:3306/project" % quote_plus("liya@1264"))
    all_data = pd.read_sql_table("analysis_data",con=engine)
    all_data=all_data.dropna(how='all')
    all_data['Order_Date_DTO']=pd.to_datetime(all_data['Order Date'],errors='coerce')
    all_data['Hour']=all_data['Order_Date_DTO'].dt.hour
    time_now = datetime.now()
    current_hour = time_now.hour
    current_data = all_data[all_data['Hour'] == current_hour]
    current_data.head()
    product_group=current_data.groupby('Product')
    quantity_ordered=product_group.sum()['Quantity Ordered']
    products=[product for product,df in product_group]
    hourly_Sale=[]
    for (index,item) in zip(products,quantity_ordered):
        hourly_Sale.append({index:item})
    return Response(hourly_Sale)
