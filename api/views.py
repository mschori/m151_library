from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author, Customer, Place, Rent


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Author.objects.all().order_by('first_name')
    serializer_class = AuthorSerializer
