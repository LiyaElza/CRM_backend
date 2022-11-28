from rest_framework import serializers

from .models import monthlyanalysis,productanalysis,orders

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

class customerOrderSerializer(serializers.Serializer):
    orderId=serializers.IntegerField()
    Amount=serializers.IntegerField()
    ProductId=serializers.IntegerField()
    ProductName=serializers.CharField(max_length=200)