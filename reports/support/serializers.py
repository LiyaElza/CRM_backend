from .models import supportlist
from rest_framework import serializers
class SupporListSerializer(serializers.ModelSerializer):
    class Meta:
        model = supportlist
        fields = '__all__'