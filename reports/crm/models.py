from django.db import models

# Create your models here.
class customers(models.Model):
    FirstName = models.CharField(max_length = 40)
    LastName = models.CharField(max_length = 40)
    Email = models.CharField(max_length = 40)
    PhoneNumber = models.BigIntegerField()