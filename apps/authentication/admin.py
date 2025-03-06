from django.contrib import admin
from django.contrib.admin import display
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = [
        "email",
        "first_name",
        "last_name",
    ]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    fieldsets = [
        [None, {"fields": ["password"]}],
        [
            _("Personal info"),
            {"fields": ["first_name", "last_name", "email", "username"]},
        ],
        [
            _("Permissions"),
            {
                "fields": [
                    "admin",
                    "staff",
                    "active",
                ],
            },
        ],
    ]

    ordering = ["-id"]
    search_fields = ("first_name", "last_name", "email", "username")
    list_filter = []
    filter_horizontal = []


admin.site.unregister(Group)
