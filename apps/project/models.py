from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel

User = get_user_model()


class Projects(BaseModel):
    name = models.CharField(max_length=245, verbose_name=_("Project Name"))
    description = models.TextField(
        verbose_name=_("Project Description"), blank=True, null=True
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("Project Owner")
    )

    class Meta:
        ordering = ["name"]
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.name


class ProjectMembers(BaseModel):
    class ROLE(models.TextChoices):
        ADMIN = "admin", _("ADMIN")
        MEMBER = "member", _("MEMBER")

    project = models.ForeignKey(
        Projects, on_delete=models.CASCADE, verbose_name=_("Project Details")
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("Project Members")
    )
    role = models.CharField(
        max_length=10, verbose_name=_("Role"), choices=ROLE.choices, default=ROLE.MEMBER
    )

    class Meta:
        ordering = ["role"]
        verbose_name = _("Project Member")
        verbose_name_plural = _("Project Members")

    def __str__(self):
        return f"{self.user} - {self.project} ({self.role})"


class Tasks(BaseModel):
    class STATUS(models.TextChoices):
        TO_DO = "to_do", _("TO_DO")
        IN_PROGRESS = "in_progress", _("IN_PROGRESS")
        DONE = "done", _("DONE")

    class PRIORITY(models.TextChoices):
        LOW = "low", _("LOW")
        MEDIUM = "medium", _("MEDIUM")
        HIGH = "high", _("HIGH")

    title = models.CharField(max_length=245, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True)
    status = models.CharField(
        max_length=25,
        verbose_name=_("Status"),
        choices=STATUS.choices,
        default=STATUS.TO_DO,
    )
    priority = models.CharField(
        max_length=25,
        verbose_name=_("Priority"),
        choices=PRIORITY.choices,
        default=PRIORITY.LOW,
    )
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("Assigned to")
    )
    project = models.ForeignKey(
        Projects, on_delete=models.CASCADE, verbose_name=_("Project Details")
    )
    due_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["due_date"]
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    def __str__(self):
        return f"{self.title} ({self.status})"


class Comments(BaseModel):
    content = models.TextField(verbose_name=_("Content"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, verbose_name=_("Task"))

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return f"Comment by {self.user} on {self.task}"
