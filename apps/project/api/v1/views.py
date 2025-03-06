from apps.project.api.base.views import (
    BaseCommentModelView,
    BaseProjectMemberModelView,
    BaseProjectModelView,
    BaseTaskModelView,
)


class ProjectModelView(BaseProjectModelView):
    pass


class ProjectMemberModelView(BaseProjectMemberModelView):
    pass


class TaskModelView(BaseTaskModelView):
    pass


class CommentModelView(BaseCommentModelView):
    pass
