from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from main.models import Firm_Recommendation


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # # still not working
    id = serializers.ReadOnlyField()
    # url = serializers.HyperlinkedIdentityField(view_name="main:user-detail")

    class Meta:
        model = User
        fields = ["url", "id", "username", "email", "is_staff"]


class FirmRecommendationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField() ## used for filtering

    class Meta:
        model = Firm_Recommendation
        fields = "__all__"
