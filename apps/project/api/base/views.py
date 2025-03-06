from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from apps.core.utils.paginator import StandardPagination
from apps.project.api.base.serializers import (
    BaseCommentModelSerializer,
    BaseProjectMemberModelSerializer,
    BaseProjectModelSerializer,
    BaseTaskModelSerializer,
    CommentGETSerializer,
    ProjectGETSerializer,
    ProjectMemberGETSerializer,
    TaskGETSerializer,
)
from apps.project.models import Comments, ProjectMembers, Projects, Tasks


class BaseProjectModelView(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = BaseProjectModelSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ProjectGETSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        user = self.request.user
        if self.action in ["update", "partial_update", "destroy"]:
            obj = Projects.objects.filter(id=self.kwargs.get("pk")).first()

            if str(user.id) != str(obj.owner.id):
                raise PermissionDenied(
                    "You do not have permission to perform this action."
                )
        return super().get_permissions()


class BaseProjectMemberModelView(viewsets.ModelViewSet):
    queryset = ProjectMembers.objects.all()
    serializer_class = BaseProjectMemberModelSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ProjectMemberGETSerializer
        return super().get_serializer_class()


class BaseTaskModelView(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = BaseTaskModelSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return TaskGETSerializer
        return super().get_serializer_class()


class BaseCommentModelView(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = BaseCommentModelSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CommentGETSerializer
        return super().get_serializer_class()
