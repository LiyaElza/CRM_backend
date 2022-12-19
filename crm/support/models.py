from django.db import models
from customers.models import customers
from products.models import productstable

class supportlist(models.Model):
    customer=models.ForeignKey(customers,on_delete=models.CASCADE)
    productname=models.ForeignKey(productstable,to_field="title",on_delete=models.CASCADE)
    supporttype=models.CharField(max_length=200)
    remarks=models.TextField()
    status=models.CharField(max_length=200)
