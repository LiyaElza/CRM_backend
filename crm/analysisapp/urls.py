from .import views
from django.urls import path
urlpatterns=[
    path('/',views.getroutes,name="routes"),
    path('adrecommendations/',views.getadrecommendation,name="adrecommendations"),
    path('productbundles/',views.getproductbundles,name="productbundles"),
    path('hourlyproductanalysis/',views.gethourlyproductanalysis,name="hourlyproductanalysis")
]