from django.urls import include, path

from apps.project.api.v1.urls import api_v1_patterns

urlpatterns = [path("api/v1/", include(api_v1_patterns))]
