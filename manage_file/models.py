import uuid

from django.db import models

from common.models import BaseModelWithUID

from .choices import STATUS_CHOICES


class FileUpload(BaseModelWithUID):
    user = models.ForeignKey(
        "core.User", on_delete=models.CASCADE, related_name="file_uploads"
    )
    file = models.FileField(upload_to="uploads/")
    filename = models.CharField(max_length=255)
    upload_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="processing"
    )
    word_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.filename} ({self.status})"


class PaymentTransaction(BaseModelWithUID):
    user = models.ForeignKey(
        "core.User", on_delete=models.CASCADE, related_name="payment_transactions"
    )
    transaction_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    gateway_response = models.JSONField(
        blank=True, null=True
    )  # Use TextField if DB doesn't support JSON
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.transaction_id} - {self.status}"


class ActivityLog(BaseModelWithUID):
    user = models.ForeignKey(
        "core.User", on_delete=models.CASCADE, related_name="activity_logs"
    )
    action = models.CharField(max_length=255)
    metadata = models.JSONField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} at {self.timestamp}"


class PaymentToken(BaseModelWithUID):
    user = models.ForeignKey(
        "core.User", on_delete=models.CASCADE, related_name="payment_tokens"
    )
    token = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    is_taken = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.is_taken}"
