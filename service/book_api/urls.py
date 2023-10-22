from django.urls import path

from .views import ListBookAPI, CreateBookAPI, UpdateDestroyBookAPI

urlpatterns = [
    path('books/', ListBookAPI.as_view()),
    path('books/create/', CreateBookAPI.as_view()),
    path('books/<int:pk>/', UpdateDestroyBookAPI.as_view()),
]
