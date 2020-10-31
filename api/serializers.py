from rest_framework import serializers
from .models import Book, Author, Customer, Place, Rent


class BookSerializer(serializers.ModelSerializer):
    author_pks = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), source='authors', write_only=True,
                                                    many=True, label='Authors')

    class Meta:
        model = Book
        fields = ('id', 'isbn', 'title', 'pages', 'is_borrowed', 'authors', 'author_pks')
        depth = 1


class AuthorSerializer(serializers.ModelSerializer):
    book_list = BookSerializer(many=True, read_only=True)
    image = serializers.ImageField(allow_null=True)

    class Meta:
        model = Author
        fields = '__all__'
        depth = 1
