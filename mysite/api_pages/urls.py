from rest_framework import routers
from .views import ItemViewSet


router = routers.DefaultRouter()
router.register('', ItemViewSet)
urlpatterns = router.urls



