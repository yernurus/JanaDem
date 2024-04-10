from rest_framework.routers import DefaultRouter
from .views import UserModelViewSet, UserCreateViewSet 


router = DefaultRouter()

router.register("", UserModelViewSet, basename="user")
router.register("register", UserCreateViewSet, basename="register")

urlpatterns = router.urls
