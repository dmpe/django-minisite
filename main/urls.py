# from main.views import LoginView
import rest_framework
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from rest_framework.authtoken import views
from rest_framework.utils import urls

from . import views
from django.contrib.auth import views as auth_views

schema_view = get_schema_view(
    openapi.Info(
        title="Finance API",
        default_version="v1",
        description="Testing django microsite",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@finance.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

app_name = "main"

# https://www.django-rest-framework.org/api-guide/routers/
router = routers.DefaultRouter()
router.register(r"user", views.UserViewSet)
router.register(r"recommendation", views.RecommendationViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("login", auth_views.LoginView.as_view(template_name='auth/login.html'), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "recommendation/edit_row/<slug:pk>/",
        views.SingleRowView.as_view(),
        name="recommendation-update",
    ),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api-token-auth/", rest_framework.authtoken.views.obtain_auth_token),
    re_path(
        "^swagger(?P<format>.json|.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path('prometheus/', include('django_prometheus.urls')),
]
