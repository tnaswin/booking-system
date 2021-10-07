from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path("login", jwt_views.TokenObtainPairView.as_view(), name="login"),
    path("run", views.HelloWorld.as_view(), name="hello-world"),
    path("user", views.Extractor.as_view(), name="user-info"),
]
