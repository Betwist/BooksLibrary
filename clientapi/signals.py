from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Client
from clientapi.tasks import send_welcome_email


@receiver(post_save, sender=Client)
def client_saved(sender, instance, **kwargs):
    send_welcome_email.delay(instance.id)