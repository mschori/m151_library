from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import BookSerializer, AuthorSerializer, PlaceSerializer, RentSerializer, CustomerSerializer, \
    UserSerializer
from .models import Book, Author, Customer, Place, Rent
from django.contrib.auth.models import User
from .permissions import IsAuthenticatedOrPostOnly


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Author.objects.all().order_by('first_name')
    serializer_class = AuthorSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Place.objects.all().order_by('postcode')
    serializer_class = PlaceSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Customer.objects.all().order_by('first_name')
    serializer_class = CustomerSerializer


class RentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Rent.objects.all().order_by('-begin')
    serializer_class = RentSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrPostOnly]

    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
