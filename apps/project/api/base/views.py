from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.core.utils.paginator import StandardPagination
from apps.project.api.base.serializers import (
    BaseCommentModelSerializer,
    BaseProjectMemberModelSerializer,
    BaseProjectModelSerializer,
    BaseTaskModelSerializer,
)
from apps.project.models import Comments, ProjectMembers, Projects, Tasks


class BaseProjectModelView(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = BaseProjectModelSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class BaseProjectMemberModelView(viewsets.ModelViewSet):
    queryset = ProjectMembers.objects.all()
    serializer_class = BaseProjectMemberModelSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class BaseTaskModelView(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = BaseTaskModelSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class BaseCommentModelView(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = BaseCommentModelSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
