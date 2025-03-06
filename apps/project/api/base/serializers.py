from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.project.models import Comments, ProjectMembers, Projects, Tasks

User = get_user_model()


# Base serializer for the Projects model
class BaseProjectModelSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Projects
        fields = "__all__"


# Base serializer for the ProjectMembers model
class BaseProjectMemberModelSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = ProjectMembers
        fields = "__all__"


# Base serializer for the Tasks model
class BaseTaskModelSerializer(serializers.ModelSerializer):
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    project = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all())

    class Meta:
        model = Tasks
        fields = "__all__"


# Base serializer for the Comments model
class BaseCommentModelSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    task = serializers.PrimaryKeyRelatedField(queryset=Tasks.objects.all())

    class Meta:
        model = Comments
        fields = "__all__"
