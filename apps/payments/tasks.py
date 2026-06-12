import time
from celery import shared_task
from .models import Payment


@shared_task
def process_payment(payment_id):
    payment = Payment.objects.get(id=payment_id)

    time.sleep(5)  # simulate delay

    payment.status = "success"
    payment.transaction_id = f"TXN-{payment.id}"
    payment.save()

    return "Payment processed"