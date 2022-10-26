from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import List


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['name', 'url', 'owner']

    # owner = serializers.StringRelatedField()
