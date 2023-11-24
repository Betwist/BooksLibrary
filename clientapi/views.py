from rest_framework import generics
from .models import Client
from .serializers import CreateClientSerializer


class ClientRegistrationView(generics.CreateAPIView):
    """Регистрация нового пользователя"""
    queryset = Client.objects.all()
    serializer_class = CreateClientSerializer
