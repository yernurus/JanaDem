from rest_framework.routers import DefaultRouter
from market.views import MarketItemModelViewSet, MarketOrderModelViewSet

#Router for market system
router = DefaultRouter()

router.register('item', MarketItemModelViewSet, basename='market-item')
router.register('order', MarketOrderModelViewSet, basename='market-order')

urlpatterns = router.urls
