from rest_framework import serializers
from .models import SellerProfile, Inventory, UserProfile, Cart


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerProfile
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
