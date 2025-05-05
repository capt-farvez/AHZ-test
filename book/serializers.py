from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    birth_date = serializers.DateField()  
    
    def create(self, validated_data):
        return Author.objects.create(**validated_data)
    

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    author = AuthorSerializer()
    published_date = serializers.DateField()
    genre = serializers.CharField(max_length=100)

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author = Author.objects.create(**author_data)
        return Book.objects.create(author=author, **validated_data)
    