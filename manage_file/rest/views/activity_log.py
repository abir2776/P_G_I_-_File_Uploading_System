from rest_framework import generics

from manage_file.models import ActivityLog

from ..serializers.activity_log_serializer import ActivityLogSerializer


class ActivityLogListAPIView(generics.ListAPIView):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer
