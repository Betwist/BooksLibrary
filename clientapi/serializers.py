from rest_framework import serializers
from .models import Client


class CreateClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['email', 'username']
