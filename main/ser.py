from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from main.models import Firm_Recommendation


class UserSerializer(serializers.HyperlinkedModelSerializer):
    lookup_field="id"
    id = serializers.ReadOnlyField()
    # url = serializers.HyperlinkedIdentityField(view_name="main:user-detail")

    class Meta:
        model = User
        fields = ["url", "id", "username", "email", "is_staff"]


class FirmRecommendationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField() ## used for filtering
    lookup_field="id"
    class Meta:
        model = Firm_Recommendation
        fields = "__all__"
