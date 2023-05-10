from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Chocolate, Cart, Favorite


# User Serializer
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email')
#
# # Register Serializer
# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
#
#         return user



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