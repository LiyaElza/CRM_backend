from rest_framework import serializers

from .models import customers
from reportsapp.models import orders,saleslist
from projectcrmapp.models import productstable

class customersSerializer(serializers.ModelSerializer):
    class Meta:
        model = customers
        fields = ('id','FirstName', 'LastName','Email','PhoneNumber','joiningDate')

