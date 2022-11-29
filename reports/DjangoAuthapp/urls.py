# from .import views
from .views import register,login,logout
from django.urls import path

app_name='DjangoAuthapp'

urlpatterns=[
    path('signup/',register,name='register'),
    path('login/',login,name="routes"),
    path('logout/',logout,name="routes")
]