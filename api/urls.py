from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path("login", jwt_views.TokenObtainPairView.as_view(), name="login"),
    path("", include("api.urls")),
]
