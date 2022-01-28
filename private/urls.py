from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PrivateViewSet


router = DefaultRouter()
router.register("users", PrivateViewSet, basename="private")
urlpatterns = router.urls
