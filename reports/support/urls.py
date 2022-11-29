from .import views
from django.urls import path

urlpatterns=[
    path('support/',views.getsupport,name="support"),
    path('editsupport/<int:pk>',views.editSupport,name="support"),
]