from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.authentication.api.base.serializers import LoginDataSerializer
from apps.project.models import Comments, ProjectMembers, Projects, Tasks

User = get_user_model()


class BaseProjectModelSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Projects
        fields = "__all__"


class ProjectGETSerializer(BaseProjectModelSerializer):
    owner = LoginDataSerializer()


class BaseProjectMemberModelSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = ProjectMembers
        fields = "__all__"


class ProjectMemberGETSerializer(BaseProjectMemberModelSerializer):
    user = LoginDataSerializer()
    project = ProjectGETSerializer()


class BaseTaskModelSerializer(serializers.ModelSerializer):
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    project = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all())

    class Meta:
        model = Tasks
        fields = "__all__"


class TaskGETSerializer(BaseTaskModelSerializer):
    assigned_to = LoginDataSerializer()
    project = ProjectGETSerializer()


class BaseCommentModelSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    task = serializers.PrimaryKeyRelatedField(queryset=Tasks.objects.all())

    class Meta:
        model = Comments
        fields = "__all__"


class CommentGETSerializer(BaseCommentModelSerializer):
    user = LoginDataSerializer()
    task = TaskGETSerializer()
