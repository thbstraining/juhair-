from django.urls import path
from . import views

urlpatterns = [
    path('authors', views.AuthorListCreate.as_view(), name='author-list-create'),
    path('authors/<int:author_id>', views.AuthorDetail.as_view(), name='author-detail'),
    path('books', views.BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:book_id>', views.BookDetail.as_view(), name='book-detail'),
]
