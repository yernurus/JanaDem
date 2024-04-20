from rest_framework import serializers

from account.serializers.user import UserSerializer
from market.models import MarketItem, MarketItemOrder

#Serializer for creating Item for Market
class CreateMarketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketItem
        fields = ['name', 'description', 'price', 'image']

#Serializer for Market Item itself
class MarketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketItem
        fields = '__all__'

#Serializer for order, to get the order firstly before redeem
class MarketItemOrderSerializer(serializers.ModelSerializer):
    item = MarketItemSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = MarketItemOrder
        fields = ['item', 'user', 'quantity', 'created_at']
