from rest_framework import serializers
from .models import offertable
class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = offertable
        fields = ('id', 'product_type', 'product','message' )