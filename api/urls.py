from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path("login", jwt_views.TokenObtainPairView.as_view(), name="login"),
    path("hello", views.HelloWorld.as_view(), name="hello-world"),
    path("user", views.UserDetails.as_view(), name="user-info"),
    path("register", views.RegisterAPI.as_view(), name="register"),
    path("delete/<int:id>", views.delete_user, name="user-delete"),
]
