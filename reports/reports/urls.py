from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('api/',include('reportsapp.urls')),
    path('app/',include('projectcrmapp.urls')),
    path('apii/', include('crm.urls')),
    path('aoffer/', include('offerapp.urls')),
    path('auth/',include('DjangoAuthapp.urls')),
    path('api2/', include('homeapp.urls')),
    path('supportapi/', include('support.urls'))
]

