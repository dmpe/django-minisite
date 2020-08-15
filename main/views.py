from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import permissions, viewsets
from main.models import Firm_Recommendation
from main.ser import FirmRecommendationSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import routers

def index(request):
    return render(request, "main/index.html", {})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    lookup_field = 'username'
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class RecommendationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Firm_Recommendation to be viewed or edited.
    """

    queryset = Firm_Recommendation.objects.all()
    serializer_class = FirmRecommendationSerializer
    permission_classes = [permissions.IsAuthenticated]



class FinanceApiRoot(APIView):

    def get(self, request, format=None):
        return Response({
            'users': reverse('user-list', request=request, format=format),
            'recommendation': reverse('recommendation-list', request=request, format=format)
        })
