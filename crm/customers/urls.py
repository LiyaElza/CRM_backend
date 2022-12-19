from .import views
from django.urls import path
urlpatterns=[  
    path('/',views.getRoutes,name="routes"),
    path('customers/',views.getcustomers,name="customers"),
    path('customerorders/',views.getcustomerdetails,name="customerorders"),
    path('customeradd/',views.addCustomer,name="customeradd"),
    path('plusCustomers/',views.plusCustomers,name="pluscustomer"),
    

   
]