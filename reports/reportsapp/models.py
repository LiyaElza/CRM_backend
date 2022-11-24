from django.db import models
# Create your models here.
class monthlyanalysis(models.Model):
    monthlist = models.CharField(max_length = 20)
    sales = models.IntegerField()

class productanalysis(models.Model):
    producttype=models.CharField(max_length=20)
    sales=models.IntegerField()
