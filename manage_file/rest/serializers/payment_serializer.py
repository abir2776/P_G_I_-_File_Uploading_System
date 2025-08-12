from rest_framework import serializers

from manage_file.models import PaymentTransaction


class PaymentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransaction
        fields = "__all__"
        read_only_fields = fields
