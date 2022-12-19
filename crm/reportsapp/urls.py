from .import views
from .views import generateCustomerReport
from django.urls import path,include
from rest_framework import routers
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'generateCustomerReport/', generateCustomerReport, basename='generateCustomerReport')

urlpatterns=[
    path('/',views.getRoutes,name="routes"),
    path('monthlysales/',views.getmonthlySales,name="monthlysales"),
    path('productsales/',views.getProductSales,name="productsales"),
    path('customersales/',views.CustomerGrowth,name="customersales"),
    path('generateProductReport/', views.generateProductReport.as_view(), name='generateProductReport'),
    path('generateMonthlyReport/', views.generateMonthlyReport.as_view(), name='generateMonthlyReport'),
    path(r'',include(router.urls))
    
]