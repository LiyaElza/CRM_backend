from django.db import models
from crm.models import customers
from projectcrmapp.models import productstable

class supportlist(models.Model):
    customer=models.ForeignKey(customers,on_delete=models.CASCADE)
    productname=models.ForeignKey(productstable,to_field="title",on_delete=models.CASCADE)
    supporttype=models.CharField(max_length=200)
    remarks=models.TextField()
    status=models.CharField(max_length=200)
