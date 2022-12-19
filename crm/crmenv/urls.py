from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('reports/',include('reportsapp.urls')),
    path('products/',include('products.urls')),
    path('customers/', include('customers.urls')),
    path('offer/', include('offerapp.urls')),
    path('auth/',include('DjangoAuthapp.urls')),
    path('home/', include('homeapp.urls')),
    path('support/', include('support.urls')),
    path('mail/',include('mailapp.urls')),
    path('analysis/',include('analysisapp.urls'))
]

