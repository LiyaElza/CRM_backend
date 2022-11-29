from django.db import models

# Create your models here.
from django.urls import reverse
class offertable(models.Model):
    id=models.IntegerField(primary_key=True)
    product_type=models.CharField(max_length=200)
    product=models.CharField(max_length=200)
    message=models.CharField(max_length=200)
    
