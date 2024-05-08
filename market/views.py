from django.db.models import Sum
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from issues.models import IssueBonusPoint
from .models import MarketItem, MarketItemOrder
from .serializers.market import CreateMarketItemSerializer, MarketItemSerializer, MarketItemOrderSerializer, CreateMarketItemOrderSerializer


#viewset for Market Item
class MarketItemModelViewSet(viewsets.ModelViewSet):
    queryset = MarketItem.objects.all()
    serializer_class = MarketItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    #function for creating Market Item
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateMarketItemSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().create(request, *args, **kwargs)
        return Response({'status': 'User is not superuser'}, status=400)

#viewset for Order 
class MarketOrderModelViewSet(viewsets.ModelViewSet):
    queryset = MarketItemOrder.objects.all()
    serializer_class = MarketItemOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    #function for getting user-dependent list of orders
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateMarketItemOrderSerializer
        return super().get_serializer_class()

    #function for creating an order while User wants to order some Market Item
    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        item_id = request.data.get('item_id')
        quantity = request.data.get('quantity')

        try:
            item = MarketItem.objects.get(pk=item_id)
        except MarketItem.DoesNotExist:
            return Response({'status': 'Item not found'}, status=400)
        #CHECKS THE USER BALANCE
        user_balance = IssueBonusPoint.objects.filter(user=request.user).aggregate(Sum('point'))['point__sum']
        my_orders = MarketItemOrder.objects.filter(user=request.user)
        for order in my_orders:
            user_balance -= order.item.price * order.quantity

        if not user_balance:
            user_balance = 0

        print(user_balance)
        if user_balance < item.price * quantity:
            return Response({'status': 'Not enough balance'}, status=400)

        #Creating an Order
        MarketItemOrder.objects.create(
            item=item,
            user=request.user,
            quantity=quantity
        )
        return Response(self.get_serializer(MarketItemOrder.objects.last()).data, status=status.HTTP_201_CREATED)
