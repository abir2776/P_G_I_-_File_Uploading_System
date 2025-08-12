from django.urls import path

from ..views.file import FileUploadCreateListAPIView

urlpatterns = [
    path("", FileUploadCreateListAPIView.as_view(), name="fileupload-list"),
]
