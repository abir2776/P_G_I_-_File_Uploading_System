from rest_framework import generics

from manage_file.models import PaymentTransaction

from ..serializers.payment_serializer import PaymentTransactionSerializer


class PaymentTransactionListAPIView(generics.ListAPIView):
    queryset = PaymentTransaction.objects.all()
    serializer_class = PaymentTransactionSerializer
