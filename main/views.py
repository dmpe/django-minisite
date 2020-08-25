from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import *
from django.shortcuts import *
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import *
from django.views.generic.edit import CreateView, UpdateView
from rest_framework import permissions, viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from main.form import RecommendationSingleRowCreateForm, RecommendationSingleRowEditForm
from main.models import Firm_Recommendation
from main.ser import FirmRecommendationSerializer, UserSerializer


class HomePage(LoginRequiredMixin, APIView):
    template_name = "main/index.html"
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            queryset = Firm_Recommendation.objects.filter(user=request.user.id)
            return Response({"recommendations": queryset})


# both have to be adjusted, becasue can view everything
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


class SingleRowEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "edit_row.html"
    model = Firm_Recommendation
    form_class = RecommendationSingleRowEditForm

    def post(self, instance, pk):
        instance = get_object_or_404(Firm_Recommendation, id=pk)
        form = RecommendationSingleRowEditForm(
            self.request.POST or None, instance=instance
        )
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("main:index")
        return render(self.request, self.template_name, {"form": form})

    # is working with 403 Forbidden
    def test_func(self):
        firm_rec_obj = self.get_object()
        return firm_rec_obj.user == self.request.user

class SingleRowCreateView(LoginRequiredMixin, CreateView):
    template_name = "add_row.html"
    model = Firm_Recommendation
    form_class = RecommendationSingleRowCreateForm

    def post(self, request, *args, **kwargs):
        new_object = RecommendationSingleRowCreateForm(request.POST, initial={"option": "10"})
        if new_object.is_valid():
            post = new_object.save(commit=False)
            post.published_date = timezone.now()
            post.user = self.request.user
            post.save()
            return redirect("main:recommendation-update", pk=post.pk)

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(self.request, self.template_name, {"form": form})


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
