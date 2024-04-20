from rest_framework.routers import DefaultRouter
from .views import IssueModelViewSet

# Router for navigating for the Issues
router = DefaultRouter()

router.register('', IssueModelViewSet, basename='issue')

urlpatterns = router.urls
