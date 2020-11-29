from rest_framework import routers

from agri.agri.api.versioned.v1.viewsets import ThirdPartyApiViewSet

router = routers.SimpleRouter()
router.register(r'third_party', ThirdPartyApiViewSet, basename='third_party',)

urlpatterns = router.urls
