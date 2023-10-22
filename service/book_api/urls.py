from django.urls import path

from .views import ListBookAPI, CreateBookAPI, UpdateDestroyBookAPI

urlpatterns = [
    path('books/', ListBookAPI.as_view(), name='books'),
    path('books/create/', CreateBookAPI.as_view(), name='create_book'),
    path('books/<int:pk>/', UpdateDestroyBookAPI.as_view(), name='update_destroy_book'),
]
