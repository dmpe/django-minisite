from django.urls import path, include
from rest_framework import routers
from main.views import *

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'recommendation', views.RecommendationViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
