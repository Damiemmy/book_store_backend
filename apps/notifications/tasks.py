from celery import shared_task

from utils.emails import send_html_email


@shared_task
def send_welcome_email_task(
    email,
    username,
):
    send_html_email(
        subject="Welcome to BookStore",
        template="emails/welcome_email.html",
        context={
            "username": username
        },
        to_email=email,
    )



@shared_task
def send_order_confirmation_email(email, username, order_id):
    send_html_email(
        subject=f"Order #{order_id} Confirmation",
        template="emails/order_confirmation.html",
        context={
            "username": username,
            "order_id": order_id,
        },
        to_email=email,
    )