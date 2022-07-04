from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import ApiViewSet


router = DefaultRouter()
router.register("api", ApiViewSet)


# Routers
urlpatterns = [
    path("", include(router.urls)),
]
