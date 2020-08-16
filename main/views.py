from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import *
from django.shortcuts import *
from django.utils import timezone
from django.shortcuts import render
from django.views import View
from django.views.generic import *
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from rest_framework import permissions, routers, status, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from main.form import RecommendationSingleRowEditForm, RecommendationSingleRowCreateForm
from main.models import Firm_Recommendation
from main.ser import FirmRecommendationSerializer, UserSerializer


# @login_required(login_url="/login")
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


class SingleRowEditView(UpdateView):
    template_name = "edit_row.html"
    model = Firm_Recommendation
    form_class = RecommendationSingleRowEditForm

    def get(self, instance, pk):
        instance = get_object_or_404(Firm_Recommendation, id=pk)
        form = RecommendationSingleRowEditForm(self.request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("main:index")
        return render(self.request, self.template_name, {"form": form})


class SingleRowCreateView(CreateView):
    template_name = "add_row.html"
    model = Firm_Recommendation
    form_class = RecommendationSingleRowCreateForm

    def post(self, request, *args, **kwargs):
        new_object = RecommendationSingleRowCreateForm(request.POST)
        if new_object.is_valid():
            post = new_object.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('main:recommendation-update', pk=post.pk)

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

class FinanceApiRoot(APIView):
    def get(self, request, format=None):
        return Response(
            {
                "user": reverse("user-list", request=request, format=format),
                "recommendation": reverse(
                    "recommendation-list", request=request, format=format
                ),
            }
        )
