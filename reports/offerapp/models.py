from django.db import models

# Create your models here.
from django.urls import reverse
from projectcrmapp.models import producttypetable,productstable
class specialoffer(models.Model):
    offer=models.TextField()
class offertable(models.Model):
    id=models.IntegerField(primary_key=True)
    product_type=models.ForeignKey(producttypetable,to_field="producttype",on_delete=models.CASCADE)
    product=models.ForeignKey(productstable,to_field="title",on_delete=models.CASCADE)
    message=models.CharField(max_length=200)
    
