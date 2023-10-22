from rest_framework import filters
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import BookModel
from .serializers import ListBookSerializer, CreateUpdateDestroyBookSerializers


class ListBookAPI(ListAPIView):
    """Вывод всех книг"""
    queryset = BookModel.objects.prefetch_related('author', 'genre')
    filter_backends = [filters.SearchFilter]
    search_fields = ['book_name', 'author__author_name', 'author__author_surname', 'genre__genre_name']
    serializer_class = ListBookSerializer


class CreateBookAPI(CreateAPIView):
    """Создание книги"""
    queryset = (
        BookModel.objects.
        values('book_name', 'price', 'description', 'author', 'genre').
        prefetch_related('author', 'genre')
    )
    serializer_class = CreateUpdateDestroyBookSerializers


class UpdateDestroyBookAPI(RetrieveUpdateDestroyAPIView):
    """Обновление или удаление книги"""
    queryset = BookModel.objects.prefetch_related('author', 'genre')
    serializer_class = CreateUpdateDestroyBookSerializers
