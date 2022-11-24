from rest_framework import serializers

from .models import monthlyanalysis,productanalysis

class MonthlySalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = monthlyanalysis
        fields = ('id','monthlist', 'sales')

class ProductSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model=productanalysis
        fields=('id','producttype','sales')