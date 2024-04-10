from django.db.models import Sum
from rest_framework import serializers

from market.models import MarketItemOrder
from ..models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email', 'birth_date', 'profile_pic', 'user_type', 'password']


class UserSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()

    def get_balance(self, obj):
        balance = obj.issuebonuspoint_set.all().aggregate(Sum('point'))['point__sum']
        my_orders = MarketItemOrder.objects.filter(user=obj)
        for order in my_orders:
            balance -= order.item.price * order.quantity

        return balance if balance else 0

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email', 'birth_date', 'profile_pic', 'user_type', 'is_active', 'balance']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email', 'birth_date', 'profile_pic', 'user_type', 'is_active']