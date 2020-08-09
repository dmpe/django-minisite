from django.contrib.auth.models import Group, User
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import permissions, viewsets

from main.ser import FirmRecommendationSerializer, UserSerializer


def index(request):
    return render(request, "main/index.html", {})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class RecommendationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = FirmRecommendationSerializer
    permission_classes = [permissions.IsAuthenticated]
