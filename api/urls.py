from django.urls import path, include
from rest_framework import routers
from . import views as api_views

routers = routers.DefaultRouter()
routers.register(r'books', api_views.BookViewSet)
routers.register(r'authors', api_views.AuthorViewSet)
routers.register(r'places', api_views.PlaceViewSet)
routers.register(r'customers', api_views.CustomerViewSet)
routers.register(r'rents', api_views.RentViewSet)
routers.register(r'users', api_views.UserViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
