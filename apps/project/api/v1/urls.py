from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.project.api.v1 import views

router = DefaultRouter()
router.register("projects", views.ProjectModelView)
router.register("project-members", views.ProjectMemberModelView)
router.register("tasks", views.TaskModelView)
router.register("comments", views.CommentModelView)


urlpatterns = [
    path("", include(router.urls)),
]
