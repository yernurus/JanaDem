from rest_framework.routers import DefaultRouter
from .views import IssueModelViewSet


router = DefaultRouter()

router.register('', IssueModelViewSet, basename='issue')

urlpatterns = router.urls
