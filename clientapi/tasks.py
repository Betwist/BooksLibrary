# tasks.py

from celery import shared_task
from django.core.mail import send_mail


from clientapi.models import Client


@shared_task
def send_welcome_email(client_id):
    client = Client.objects.get(pk=client_id)

    subject = 'Добро пожаловать'
    message = f'Спасибо за регистрацию, {client.username}!'
    from_email = 'your_email@example.com'  # Укажите ваш адрес электронной почты
    to_email = [client.email]

    # send_mail(subject, message, from_email, to_email)
