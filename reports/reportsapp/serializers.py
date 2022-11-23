from rest_framework import serializers

from .models import monthlyanalysis

class MonthlySalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = monthlyanalysis
        fields = ('id','monthlist', 'sales')