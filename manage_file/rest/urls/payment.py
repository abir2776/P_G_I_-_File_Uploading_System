from django.urls import path

from ..views.payment import PaymentTransactionListAPIView

urlpatterns = [
    path("", PaymentTransactionListAPIView.as_view(), name="payment-list"),
]
