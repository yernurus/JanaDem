from rest_framework import serializers

from account.serializers.user import UserSerializer
from market.models import MarketItem, MarketItemOrder


class CreateMarketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketItem
        fields = ['name', 'description', 'price', 'image']


class MarketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketItem
        fields = '__all__'


class MarketItemOrderSerializer(serializers.ModelSerializer):
    item = MarketItemSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = MarketItemOrder
        fields = ['item', 'user', 'quantity', 'created_at']
