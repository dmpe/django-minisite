from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import *
from django.shortcuts import *
from django.shortcuts import render
from django.views import View
from django.views.generic import *
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from rest_framework import permissions, routers, status, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from main.form import RecommendationSingleRowForm
from main.models import Firm_Recommendation
from main.ser import FirmRecommendationSerializer, UserSerializer


# @login_required(login_url="/login")
def index(request):
    return render(request, "main/index.html", {})


# class LoginView(View):
#     """
#     Uses class based view
#     """

#     template_name = "auth/login.html"

#     def post(self, request, *args, **kwargs):
#         # recieve
#         username_email = request.POST.get("email", False)
#         user_password = request.POST.get("password", False)

#         try:
#             auth_user = authenticate(
#                 self, request, username=username_email, password=user_password
#             )

#             if auth_user is None:
#                 messages.add_message(
#                     request,
#                     messages.WARNING,
#                     mark_safe(
#                         "<h4 class="
#                         "alert-heading"
#                         ">Such a user does not exist.</h4>"
#                         "<p>Make sure that username and password are correct.</p>"
#                     ),
#                 )
#             else:
#                 try:
#                     # whether the user is active or not is already checked by the
#                     # ModelBackend we use
#                     django_login(request, auth_user, backend="core.backends.EmailUserNameAuthBackend")
#                     return redirect("userMng:userMng_index")
#                 except Exception as e:
#                     raise e

#         except Exception as e:
#             raise e
#         # user is bot
#         # else:
#         #     messages.add_message(
#         #         request,
#         #         messages.WARNING,
#         #         mark_safe(
#         #             "<h4 class="
#         #             "alert-heading"
#         #             ">Sorry, but you seem to be a computer bot.</h4>"
#         #             "<p>Please contact us if you believe you were wrongly identified because of Google Recaptha v3.</p>"
#         #             "<p>Solution: clear your cookies and try again.</p>"
#         #         ),
#         #     )

#         return render(request, self.template_name)

#     def get(self, request, *args, **kwargs):
#         # if get request just render the template, with form
#         return render(request, self.template_name)

# class LogoutView(View):
#     """
#     Class based view for logout
#     Only requires get method
#     """

#     def get(self, request):
#         logout(request)
#         return redirect("main:login")


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
    form_class = RecommendationSingleRowForm

    def get(self, instance, pk):
        instance = get_object_or_404(Firm_Recommendation, id=pk)
        form = RecommendationSingleRowForm(self.request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("main:index")
        return render(self.request, self.template_name, {"form": form})

    # def get(self, request, *args, **kwargs):
    #     display_bject = Firm_Recommendation.objects.get(pk=pk)
    #     return render(request, self.template_name, {"form": display_bject})


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
