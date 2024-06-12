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


class CreateMarketItemOrderSerializer(serializers.Serializer):
    item_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class MyOrdersItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketItem
        fields = ['name', 'price', 'image']


class MyOrdersSerializer(serializers.ModelSerializer):
    item = MyOrdersItemSerializer(read_only=True)
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = MarketItemOrder
        fields = ['item', 'quantity', 'created_at']
