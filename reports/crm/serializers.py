from rest_framework import serializers

from .models import customers

class customersSerializer(serializers.ModelSerializer):
    class Meta:
        model = customers
        fields = ('id','FirstName', 'LastName','Email','PhoneNumber','joiningDate')

