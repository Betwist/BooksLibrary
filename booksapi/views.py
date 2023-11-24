from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


class BookListCreateView(generics.ListCreateAPIView):
    """Получение информации о всех книгах и добавление новой"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Получение, обновление и удаление конкретной книги"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
