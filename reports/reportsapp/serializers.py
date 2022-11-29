from rest_framework import serializers

from .models import monthlyanalysis,productanalysis,orders,saleslist

class MonthlySalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = monthlyanalysis
        fields = ('id','monthlist', 'sales')

class ProductSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model=productanalysis
        fields=('id','producttype','sales')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=orders
        fields='__all__'


class SalesListSerializer(serializers.Serializer):
    class Meta:
        model=saleslist
        fields='__all__'

