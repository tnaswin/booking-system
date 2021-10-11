from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import UserSerializer, RegisterSerializer


class HelloWorld(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {"message": "Hello World"}
        return Response(content)


class UserDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {
            "username": request.user.username,
            "password": request.user.password,
        }
        return Response(content)


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
            }
        )


@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def delete_user(request, id):
    user = User.objects.get(id=id)
    if request.method == "DELETE":
        # user.delete()
        user.is_active = False
        user.save()
        return Response({"message": "User deleted"})
