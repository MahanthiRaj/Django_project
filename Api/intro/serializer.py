from rest_framework import serializers
from .models import intro

class introSerializer(serializers.ModelSerializer):
    class Meta:
        model = intro
        fields = '__all__'
