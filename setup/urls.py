from django.contrib import admin
from django.urls import path

from books.views import BooksListView, BooksCreateView

urlpatterns = [
    path("admin/", admin.site.urls), 
    path("", BooksListView.as_view(), name="books_list"),
    path("create", BooksCreateView.as_view(), name="books_create"),
]
