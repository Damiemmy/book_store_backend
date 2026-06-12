from django.template.loader import render_to_string
from django.utils.timezone import now
from django.conf import settings
from django.core.mail import EmailMessage


def send_html_email(
    *,  #forces key and values to be attached or present
    subject,
    template,
    context,
    to_email,
):
    context["year"] = now().year

    html_content = render_to_string(
        template,
        context,
    )

    email = EmailMessage(
        subject=subject,
        body=html_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[to_email],
    )

    email.content_subtype = "html"

    email.send()