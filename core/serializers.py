from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import List, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'List', 'done', 'url']


class ListSerializer(serializers.ModelSerializer):
    item_set = ItemSerializer(many=True)

    class Meta:
        model = List
        fields = ['owner', 'name', 'url', 'item_set']

    # owner = serializers.StringRelatedField()
