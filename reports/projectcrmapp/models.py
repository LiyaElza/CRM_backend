from django.db import models

# Create your models here.
from django.urls import reverse
# Create your models here.
class productstable(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length = 200)
    category = models.CharField(max_length = 200)
    thiruvalla = models.IntegerField()
    kottayam = models.IntegerField()
    kochi = models.IntegerField()
    img = models.CharField(max_length = 300)

    objects=models.Manager()

