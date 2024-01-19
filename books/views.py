from django.shortcuts import render
from .models import Books

def books_list(request):
    books = Books.objects.all()

    return render(request, "books/books_list.html", {"books": books})
