from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from testapp.models import Book
from django.urls import reverse_lazy

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'testapp/books.html'
    context_object_name = 'books'

class BookListView2(ListView):
    model = Book
    template_name = 'testapp/books.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book

class BookCreateView(CreateView):
    model = Book
    fields = '__all__'

class BookUpdateView(UpdateView):
    model = Book
    fields = ('pages', 'price')

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('listbooks')