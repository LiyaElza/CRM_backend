from rest_framework import serializers
from .models import offertable,specialoffer
class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = offertable
        fields = ('id', 'product_type', 'product','message' )

class SpecialOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model=specialoffer
        fields=("id","offer")