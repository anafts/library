from django.contrib import admin
from django.urls import path

from books.views import BooksListView, BooksCreateView, BooksUpdateView, BooksDeleteView, search_list

urlpatterns = [
    path("admin/", admin.site.urls), 
    path("search/", search_list, name="books_search"),
    path("", BooksListView.as_view(template_name="books_list"), name="books_list"),
    path("create", BooksCreateView.as_view(), name="books_create"),
    path("update/<int:pk>", BooksUpdateView.as_view(), name="books_update"),
    path("delete/<int:pk>", BooksDeleteView.as_view(), name="books_delete"),
]
