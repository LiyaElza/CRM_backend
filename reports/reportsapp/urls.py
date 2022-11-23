from .import views
from django.urls import path

urlpatterns=[
    path('',views.getRoutes,name="routes"),
    path('monthlysales/',views.getmonthlySales,name="monthlysales"),
]