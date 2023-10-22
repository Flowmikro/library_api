from rest_framework import serializers

from .models import BookModel


class ListBookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='author_surname', read_only=True, many=True)
    genre = serializers.SlugRelatedField(slug_field='genre_name', read_only=True, many=True)

    class Meta:
        model = BookModel
        fields = ('id', 'book_name', 'price', 'description', 'author', 'genre')


class CreateUpdateDestroyBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('book_name', 'description', 'price', 'author', 'genre')
