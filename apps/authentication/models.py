from django.contrib.auth.models import AbstractBaseUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.authentication.manager import UserManager


# User model
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=245, verbose_name=_("first name"))
    last_name = models.CharField(max_length=245, verbose_name=_("last name"))
    email = models.EmailField(max_length=245, unique=True, verbose_name=_("email"))
    username = models.CharField(max_length=245, unique=True, verbose_name=_("username"))
    date_joined = models.DateTimeField(auto_now_add=True)

    # user authorizations and activity information
    admin = models.BooleanField(default=False, verbose_name=_("is admin"))
    staff = models.BooleanField(default=False, verbose_name=_("is staff"))
    active = models.BooleanField(default=False, verbose_name=_("is active"))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ("-id",)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        if self.staff == True:
            return True
        else:
            return False

    @property
    def is_superuser(self):
        if self.admin == True:
            return True
        else:
            return False

    @property
    def is_admin(self):
        if self.admin == True:
            return True
        else:
            return False
