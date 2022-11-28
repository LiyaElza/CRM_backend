from .import views
from django.urls import path

urlpatterns=[
    path('/',views.getRoutes,name="routes"),
    path('monthlysales/',views.getmonthlySales,name="monthlysales"),
    path('productsales/',views.getProductSales,name="productsales"),
    path('customersales/',views.CustomerGrowth,name="customersales"),
    path('generateProductReport/', views.generateProductReport.as_view(), name='generateProductReport'),
    path('generateMonthlyReport/', views.generateMonthlyReport.as_view(), name='generateMonthlyReport'),
    path('generateCustomerReport/', views.generateCustomerReport.as_view(), name='generateCustomerReport')
    
]