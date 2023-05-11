from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Chocolate, Cart, Favorite

class ChocoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chocolate
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    items = ChocoSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'items')

class FavoriteSerializer(serializers.ModelSerializer):
    items = ChocoSerializer(many=True, read_only=True)

    class Meta:
        model = Favorite
        fields = ('id', 'items')