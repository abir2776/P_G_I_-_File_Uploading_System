from django.urls import path

from ..views.activity_log import ActivityLogListAPIView

urlpatterns = [
    path("", ActivityLogListAPIView.as_view(), name="activity-log-list"),
]
