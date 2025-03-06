from apps.authentication.api.base.views import (
    BaseLoginAPIView,
    BaseUserChangePasswordAPIView,
    BaseUserModelView,
    BaseUserRegisterAPIView,
)


class UserRegisterAPIView(BaseUserRegisterAPIView):
    pass


class LoginAPIView(BaseLoginAPIView):
    pass


class UserChangePasswordAPIView(BaseUserChangePasswordAPIView):
    pass


class UserModelView(BaseUserModelView):
    pass
