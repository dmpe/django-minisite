from django.urls import include, path
import rest_framework
from rest_framework import routers
from rest_framework.authtoken import views

from . import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"recommendation", views.RecommendationViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("", include(router.urls, namespace='main')),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api-token-auth/", rest_framework.authtoken.views.obtain_auth_token),
]
