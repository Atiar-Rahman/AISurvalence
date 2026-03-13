from rest_framework.routers import DefaultRouter
from api.views import HomeViewSet
from cameras.views import CameraViewSet

router = DefaultRouter()
router.register('', HomeViewSet, basename='home')
router.register('cameras',CameraViewSet,basename='camera')

urlpatterns = router.urls