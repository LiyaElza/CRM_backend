from rest_framework import serializers

from .models import monthlyanalysis,productanalysis,saleslist

class MonthlySalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = monthlyanalysis
        fields = ('id','monthlist', 'sales')

class ProductSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model=productanalysis
        fields=('id','producttype','sales')
class SalesListSerializer(serializers.ModelSerializer):
      class Meta:
        model=saleslist
        fields=('orderid','productid','producttype','quantity')