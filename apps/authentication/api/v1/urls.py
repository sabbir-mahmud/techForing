from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from apps.authentication.api.v1 import views

router = DefaultRouter()
router.register("user", views.UserModelView, basename="user-detail")

api_v1_patterns = [
    path("", include(router.urls)),
    path("register/", views.UserRegisterAPIView.as_view()),
    path("login/", views.LoginAPIView.as_view()),
    path("change-password/", views.UserChangePasswordAPIView.as_view()),
]
