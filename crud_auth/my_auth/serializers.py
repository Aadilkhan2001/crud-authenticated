import imp
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cart


class UserSerializer(serializers.ModelSerializer):
    # cart = serializers.PrimaryKeyRelatedField(many=True,queryset=Cart.objects.all())
    class Meta:
        model = User
        fields=['id','username']
        read_only_fields = (['id'])

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','user','product','quantity','price']
        read_only_fields = (['user','id'])

