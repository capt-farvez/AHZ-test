from django.urls import path

from .views import (
    AuthorCreateView, 
    AuthorView, 
    AuthorDetailView, 
    BookCreateView, 
    BookView, 
    BookDetailView,
    GetBookByAuthorNameView
)

urlpatterns = [
    path('authors/create/', AuthorCreateView.as_view(), name='author-create'),
    path('authors/', AuthorView.as_view(), name='author-list'),
    path('authors/<int:id>/', AuthorDetailView.as_view(), name='author-detail'),

    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/', BookView.as_view(), name='book-list'),
    path('books/<int:id>/', BookDetailView.as_view(), name='book-detail'),
    path('books/author/<str:author_name>/', GetBookByAuthorNameView.as_view(), name='books-by-author-name'),
]