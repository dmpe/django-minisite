import django.contrib.auth.models
from main.models import Firm_User, Firm_Recommendation
from rest_framework import serializers


class FirmUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Firm_User
        fields = ['short_username', 'first_name', 'second_name', 'email']


class FirmRecommendationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Firm_Recommendation
        fields = ['name']
