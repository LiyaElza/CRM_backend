from rest_framework import serializers

<<<<<<< HEAD
from .models import monthlyanalysis,productanalysis,saleslist
=======
from .models import monthlyanalysis,productanalysis,orders
>>>>>>> ebf1d2bdb7a689eb3508ea807dd4e2c80baca73c

class MonthlySalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = monthlyanalysis
        fields = ('id','monthlist', 'sales')

class ProductSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model=productanalysis
        fields=('id','producttype','sales')
<<<<<<< HEAD
class SalesListSerializer(serializers.ModelSerializer):
      class Meta:
        model=saleslist
        fields=('orderid','productid','producttype','quantity')
=======

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=orders
        fields='__all__'

class customerOrderSerializer(serializers.Serializer):
    orderId=serializers.IntegerField()
    Amount=serializers.IntegerField()
    ProductId=serializers.IntegerField()
    ProductName=serializers.CharField(max_length=200)
>>>>>>> ebf1d2bdb7a689eb3508ea807dd4e2c80baca73c
