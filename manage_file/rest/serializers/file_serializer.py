from rest_framework import serializers

from manage_file.models import FileUpload


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = [
            "user",
            "file",
            "upload_time",
            "status",
            "word_count",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "user",
            "upload_time",
            "status",
            "word_count",
            "created_at",
            "updated_at",
        ]
