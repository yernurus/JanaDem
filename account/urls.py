from rest_framework.routers import DefaultRouter
from .views import UserModelViewSet

#Router for navigating 

router = DefaultRouter()

router.register("", UserModelViewSet, basename="user")

urlpatterns = router.urls
