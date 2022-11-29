from .import views
from django.urls import path
urlpatterns=[
    path('/',views.getroutes,name="routes"),
    path('offer/',views.getoffer,name="offer")

 
]  