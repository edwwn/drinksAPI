from dataclasses import fields
from rest_framework import serializers
from .models import Drink

class DrinkSerialializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']
        
