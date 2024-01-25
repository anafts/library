from .models import Books
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

class BooksListView(ListView):
    model = Books


class BooksCreateView(CreateView):
    model = Books
    fields = [ "title", "author", "gender", "pages", "copies", "isbn", "description", "publishing_company"]
    success_url = reverse_lazy("books_list")

class BooksUpdateView(UpdateView):
    model = Books
    fields = [ "title", "author", "gender", "pages", "copies", "isbn", "description", "publishing_company"]
    success_url = reverse_lazy("books_list")
