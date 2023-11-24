
import os

from django.core.mail import send_mail

from BooksLibrary.celery import app
from clientapi.models import Client
from dotenv import load_dotenv

load_dotenv()


@app.task
def send_welcome_email(client_id):
    client = Client.objects.get(pk=client_id)

    subject = 'Добро пожаловать'
    message = f'Спасибо за регистрацию, {client.username}!'
    from_email = os.environ.get('EMAIL_HOST_USER')  # Укажите ваш адрес электронной почты
    to_email = [client.email]
    send_mail(subject, message, from_email, to_email)
