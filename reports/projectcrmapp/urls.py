from .import views
from django.urls import path
urlpatterns=[
    path('/',views.getroutes,name="routes"),
    path('products/',views.getproducts,name="products")
    # path('products/',views.getproducts,name="products"),
    # path('products/<str:pk>',views.getproducts,name="product"),
    # path('meals/',views.getmealss,name="meals"),
    # path('meals/<str:pk>',views.getmeals,name="meals"),

]   