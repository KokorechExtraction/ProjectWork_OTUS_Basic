from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_info_email(recipient_email, subject, message):
    send_mail(
        subject=subject,
        message=message,
        from_email='1@1.ru',
        recipient_list=[recipient_email],
    )
    return f'Почта отправлена {recipient_email}'


