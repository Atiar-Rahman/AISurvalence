from rest_framework.routers import DefaultRouter
from api.views import HomeViewSet
from cameras.views import CameraViewSet
from alert.views import NotificationViewSet

router = DefaultRouter()
router.register('', HomeViewSet, basename='home')
router.register('cameras',CameraViewSet,basename='camera')
router.register('notification',NotificationViewSet,basename='notification')


urlpatterns = router.urls