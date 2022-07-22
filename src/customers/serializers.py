from rest_framework import serializers
from .models import Client

class CreateTenantSerializer(serializers.ModelSerializer):
    """serializer class to create tenant"""
    class Meta:
        """pass"""
        model = Client
        fields = ('name',)
        