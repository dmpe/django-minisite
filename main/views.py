from django.contrib.auth.models import User
from django.http import *
from django.shortcuts import render
from rest_framework import permissions, viewsets
from main.models import Firm_Recommendation
from main.form import RecommendationSingleRowForm
from main.ser import FirmRecommendationSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import routers
from django.shortcuts import *
from django.views import View
from django.views.generic import *
from django.views.generic.edit import CreateView, DeleteView, UpdateView

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
    API endpoint that allows Firm_Recommendation to be viewed or edited.
    """

    queryset = Firm_Recommendation.objects.all()
    serializer_class = FirmRecommendationSerializer
    permission_classes = [permissions.IsAuthenticated]


class SingleRowView(UpdateView):
    template_name = "edit_row.html"
    model = Firm_Recommendation

    def post(self, instance, id):
        instance = get_object_or_404(Firm_Recommendation, id=id)
        form = RecommendationSingleRowForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('main:index')
        return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class FinanceApiRoot(APIView):

    def get(self, request, format=None):
        return Response({
            'user': reverse('user-list', request=request, format=format),
            'recommendation': reverse('recommendation-list', request=request, format=format)
        })
