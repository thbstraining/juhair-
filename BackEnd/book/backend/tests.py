from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author1 = Author.objects.create(name="Author One", bio="Bio of Author One")
        self.author2 = Author.objects.create(name="Author Two", bio="Bio of Author Two")
        self.author_list_url = '/api/authors/'
        self.author_detail_url = lambda author_id: f'/api/authors/{author_id}/'

    def test_list_authors(self):
        response = self.client.get(self.author_list_url)
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"authors": serializer.data})

    def test_create_author(self):
        data = {'name': 'Author Three', 'bio': 'Bio of Author Three'}
        response = self.client.post(self.author_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 3)
        self.assertEqual(Author.objects.get(id=response.data['id']).name, 'Author Three')

    def test_get_author_by_id(self):
        response = self.client.get(self.author_detail_url(self.author1.id))
        serializer = AuthorSerializer(self.author1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_author_by_invalid_id(self):
        response = self.client.get(self.author_detail_url(999))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class BookTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name="Author One", bio="Bio of Author One")
        self.book1 = Book.objects.create(title="Book One", genre="Fiction", author=self.author)
        self.book2 = Book.objects.create(title="Book Two", genre="Non-Fiction", author=self.author)
        self.book_list_url = '/api/books/'
        self.book_detail_url = lambda book_id: f'/api/books/{book_id}/'

    def test_list_books(self):
        response = self.client.get(self.book_list_url)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"books": serializer.data})

    def test_create_book(self):
        data = {'title': 'Book Three', 'genre': 'Fantasy', 'author': self.author.id}
        response = self.client.post(self.book_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'Book Three')

    def test_get_book_by_id(self):
        response = self.client.get(self.book_detail_url(self.book1.id))
        serializer = BookSerializer(self.book1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_book_by_invalid_id(self):
        response = self.client.get(self.book_detail_url(999))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
