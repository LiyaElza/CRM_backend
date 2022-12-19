from django.db import models
from customers.models import customers
from products.models import productstable,producttypetable
# Create your models here.
class monthlyanalysis(models.Model):
    monthlist = models.CharField(max_length = 20)
    sales = models.IntegerField()

class productanalysis(models.Model):
    producttype=models.CharField(max_length=20)
    sales=models.IntegerField()

class orders(models.Model):
    orderid=models.IntegerField(primary_key=True)
    customerid=models.ForeignKey(customers, on_delete=models.CASCADE)
    orderDate=models.DateTimeField()
    amount=models.IntegerField()

class saleslist(models.Model):
    orderid=models.ForeignKey(orders,on_delete=models.CASCADE)
    productid=models.ForeignKey(productstable,on_delete=models.CASCADE)
    producttype=models.ForeignKey(producttypetable,to_field="producttype",on_delete=models.CASCADE)
    quantity=models.IntegerField()

    class Meta :
        unique_together = (('orderid','productid'),)
