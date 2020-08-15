from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from main.models import Firm_Recommendation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class FirmRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm_Recommendation
        fields = "__all__"
