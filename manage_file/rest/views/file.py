from rest_framework import generics

from manage_file.models import FileUpload

from ..serializers.file_serializer import FileUploadSerializer


class FileUploadCreateListAPIView(generics.ListCreateAPIView):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
