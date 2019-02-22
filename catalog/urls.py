from django.urls import path
from . import views
from catalog.models import Book, Author, BookInstance, Genre

urlpatterns = [
    path('', views.index, name='index'),
]
