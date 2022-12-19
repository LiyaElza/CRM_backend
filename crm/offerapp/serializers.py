from rest_framework import serializers
from .models import offertable,specialoffer
class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = offertable
        fields = '__all__'

class SpecialOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model=specialoffer
        fields='__all__'