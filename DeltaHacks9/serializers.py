from rest_framework import serializers
from .models import BigBuisness

class DeltaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BigBuisness
        fields = ['id', 'name']