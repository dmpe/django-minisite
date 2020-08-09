from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from main.models import Firm_Recommendation


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="main:user-detail")

    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


class FirmRecommendationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Firm_Recommendation
        fields = "__all__"
