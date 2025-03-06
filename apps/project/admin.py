from django.contrib import admin

from apps.project.models import Comments, ProjectMembers, Projects, Tasks


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "description")
    search_fields = ("name", "description")
    list_filter = ("owner",)


@admin.register(ProjectMembers)
class ProjectMembersAdmin(admin.ModelAdmin):
    list_display = ("project", "user", "role")
    search_fields = ("project__name", "user__username", "role")
    list_filter = ("role",)


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "priority", "assigned_to", "project", "due_date")
    search_fields = ("title", "status", "priority", "assigned_to__username")
    list_filter = ("status", "priority", "assigned_to", "project", "due_date")


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("task", "user", "content", "created_at")
    search_fields = ("content", "user__username", "task__title")
    list_filter = ("created_at", "user", "task")
