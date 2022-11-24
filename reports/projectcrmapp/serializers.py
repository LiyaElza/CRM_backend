from rest_framework import serializers

from .models import productstable

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = productstable
        fields = ('id', 'title', 'category','thiruvalla','kottayam','kochi', 'img' )