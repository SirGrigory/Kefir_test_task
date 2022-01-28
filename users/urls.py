from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet


urlpatterns = [
    path("", UserViewSet.as_view({"get": "list"})),
    path("<int:pk>/", UserViewSet.as_view({"patch": "partial_update"})),
    path("current/", UserViewSet.as_view({"get": "retrieve"})),
]
