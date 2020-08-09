from django.contrib.auth.models import User
from main.models import Firm_Recommendation
from rest_framework import serializers, viewsets, routers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class FirmRecommendationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Firm_Recommendation
        fields = '__all__'
