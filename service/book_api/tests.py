from django.urls import reverse
from rest_framework.test import APITestCase
from .models import BookModel, AuthorModel, GenreModel


class ListBookAPITest(APITestCase):
    def test_get_all_books(self):
        url = reverse('books')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class CreateBookAPITest(APITestCase):
    def setUp(self):
        self.author = AuthorModel.objects.create(author_name='John', author_surname='Doe')
        self.genre = GenreModel.objects.create(genre_name='Fantasy')

    def test_create_book(self):
        data = {
            'book_name': 'New Book',
            'description': 'Description of New Book',
            'price': 100,
            'author': [self.author.id],
            'genre': [self.genre.id]
        }
        url = reverse('create_book')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(BookModel.objects.count(), 1)


class UpdateDestroyBookAPITest(APITestCase):
    def setUp(self):
        self.author = AuthorModel.objects.create(author_name='John', author_surname='Doe')
        self.genre = GenreModel.objects.create(genre_name='Fantasy')
        self.book = BookModel.objects.create(book_name='Book', description='Description', price=100)

    def test_update_book(self):
        data = {
            'book_name': 'Updated Book',
            'description': 'Updated Description',
            'price': 200,
            'author': [self.author.id],
            'genre': [self.genre.id]
        }
        url = reverse('update_destroy_book', args=[self.book.id])
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.book.refresh_from_db()
        self.assertEqual(self.book.book_name, 'Updated Book')
        self.assertEqual(self.book.description, 'Updated Description')
        self.assertEqual(self.book.price, 200)

    def test_delete_book(self):
        url = reverse('update_destroy_book', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(BookModel.objects.count(), 0)

