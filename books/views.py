from django.shortcuts import render
from .models import Books
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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

class BooksDeleteView(DeleteView):
    model = Books
    success_url = reverse_lazy("books_list")

def search_list(request):

    if request.method == 'POST':
        searched = request.POST['searched']
        books = Books.objects.filter(title__contains = searched)

        return render(request, 
        'books/search_list.html', {'searched': searched, 'books': books})
    else:
        return render(request, 
        'books/search_list.html', {})