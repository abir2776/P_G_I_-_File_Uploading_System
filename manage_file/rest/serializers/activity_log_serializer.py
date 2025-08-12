from rest_framework import serializers

from manage_file.models import ActivityLog


class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = "__all__"
        read_only_fields = fields 
