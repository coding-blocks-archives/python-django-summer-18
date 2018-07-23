from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from . import models

# Create your views here.

class SuccessView(TemplateView):
    template_name = 'main/success.html'

class Index(TemplateView):
    template_name = "main/index.html"

class BookList(ListView):
    model = models.Book
    template_name = 'main/book_list.html'
    context_object_name = 'books'

class BookDetail(DetailView):
    model = models.Book
    context_object_name = 'book'

    def get_context_data(self, object):
        context = super().get_context_data()

        context['name'] = "Jatin Katyal"

        return context

    # def post(self, request):




class PublisherList(ListView):
    model = models.Publisher
    context_object_name = 'publishers'

class PublisherDetail(DetailView):
    model = models.Publisher
    context_object_name = 'publisher'

class PublisherBooksList(ListView):
    template_name = 'main/publisher_book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        self.publisher = get_object_or_404(models.Publisher, name = self.kwargs['publisher'])
        return models.Book.objects.filter(publisher = self.publisher)



class AuthorList(ListView):
    model = models.Author
    context_object_name = 'authors'

class AuthorDetail(DetailView):
    model = models.Author
    context_object_name = 'author'

class CreateAuthor(CreateView):
    model = models.Author
    fields = '__all__'
    success_url = '/success/'

    def form_valid(self, form):

        print("Donzo !")

        return super().form_valid(form)

class UpdateAuthor(UpdateView):
    model = models.Author
    fields = '__all__'
    success_url = '/success/'
    