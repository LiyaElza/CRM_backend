from .import views
from django.urls import path

urlpatterns=[
    path('/',views.getRoutes,name="routes"),
    path('monthlysales/',views.getmonthlySales,name="monthlysales"),
    path('productsales/',views.getProductSales,name="productsales"),
    path('generateProductReport/', views.generateProductReport, name='generateProductReport'),
    path('generateMonthlyReport/', views.generateMonthlyReport, name='generateMonthlyReport')
]