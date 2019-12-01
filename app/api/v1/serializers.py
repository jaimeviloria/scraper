from rest_framework import serializers
from core.models import Item

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        lookup_field = 'item_uuid'
        fields = ('item_uuid','item_name')

