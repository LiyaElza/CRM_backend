from django.db import models

# Create your models here.
from django.urls import reverse
# Create your models here.
class producttypetable(models.Model):
    producttype=models.CharField(max_length=200,unique=True)


class productstable(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length = 200,unique=True)
    category = models.ForeignKey(producttypetable,to_field="producttype",on_delete=models.CASCADE)
    thiruvalla = models.IntegerField()
    kottayam = models.IntegerField()
    kochi = models.IntegerField()
    img = models.CharField(max_length = 300)

