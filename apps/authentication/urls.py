from django.urls import include, path

from apps.authentication.api.v1.urls import api_v1_patterns

urlpatterns = [path("api/v1/", include(api_v1_patterns))]
