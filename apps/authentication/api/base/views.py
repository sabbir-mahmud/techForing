from django.contrib.auth import authenticate, get_user_model, login, logout
from rest_framework import status, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from apps.authentication.api.base.serializers import (
    BaseUserSerializer,
    LoginDataSerializer,
    LoginSerializer,
    PasswordChangeSerializer,
    RegisterSerializer,
)

User = get_user_model()


def jwt_generator(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class BaseUserRegisterAPIView(APIView):

    def post(self, request, format=None):
        sr = RegisterSerializer(data=request.data)
        sr.is_valid(raise_exception=True)
        user = sr.save()

        login(request, user)
        user.login_tried = 0
        user.save()
        context = {"status": "account created!"}
        return Response(context, status=status.HTTP_201_CREATED)


class BaseLoginAPIView(APIView):
    def post(self, request):
        sr = LoginSerializer(data=request.data)
        sr.is_valid(raise_exception=True)

        email = sr.data["email"]
        password = sr.data["password"]
        user = authenticate(username=email, password=password)
        login(request, user)

        token = jwt_generator(user)

        context = {
            "message": "login successful",
            "token": {
                "access_token": token["access"],
                "refresh_token": token["refresh"],
            },
            "user": LoginDataSerializer(user).data,
        }
        return Response(context)


class BaseUserChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = PasswordChangeSerializer(
            data=request.data, context={"user": request.user}
        )
        serializer.is_valid(raise_exception=True)
        context = {"message": "Password Changed Successfully"}
        return Response(context, status=status.HTTP_202_ACCEPTED)


class BaseUserModelView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = (
        LoginDataSerializer  # BaseUserSerializer removed to protect password
    )
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return LoginDataSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        user = self.request.user

        if self.action in ["retrieve", "update", "partial_update", "destroy"]:
            obj_id = self.kwargs.get("pk")
            if str(user.id) != str(obj_id):
                raise PermissionDenied(
                    "You do not have permission to perform this action."
                )

        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        return Response(
            {"detail": "Listing users is not allowed."},
            status=status.HTTP_403_FORBIDDEN,
        )
