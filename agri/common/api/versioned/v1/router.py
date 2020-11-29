from django.urls import path, include
from agri.agri.api.versioned.v1.routers import router

urlpatterns = [
    path('', include(router.urls)),
]
