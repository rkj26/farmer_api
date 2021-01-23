from rest_framework import serializers
from .models import SellerProfile, Inventory

class SellerSerializer(serializers.ModelSerializer):
  class Meta:
    model = SellerProfile
    fields = ('__all__')

class InventorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Inventory
    fields = ('__all__')