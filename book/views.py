from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

#  Authors APi
class AuthorCreateView(APIView):
    # API endpoint for creating authors '''
    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorView(generics.ListAPIView):
    #  API endpoint for listing authors
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_class =[]       

class AuthorDetailView(generics.RetrieveAPIView):
    # API endpoint for detail about specific author '''
    def get_object(self):
        slug = self.kwargs["id"]
        obj = get_object_or_404(Author, id=id)
        return obj
    

 # Books API
class BookCreateView(APIView):
    # API endpoint for creating books '''
    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class BookView(generics.ListAPIView):
    #  API endpoint for listing books '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class =[]

class BookDetailView(generics.RetrieveAPIView):
    #  API endpoint for detail about specific book '''
    def get_object(self):
        slug = self.kwargs["id"]
        obj = get_object_or_404(Book, id=id)
        return obj
    
class GetBookByAuthorNameView(APIView):
    # API endpoint for getting books by author name '''
    def get(self, request, author_name, format=None):
        books = Book.objects.filter(author__name=author_name)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)