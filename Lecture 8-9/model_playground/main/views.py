from django.shortcuts import render
from django.http import HttpResponse

# import models
from .models import Book

# import forms
from .forms import BookForm

# Create your views here.

def index(request):
	return HttpResponse("Hello World")

def book_form(request):

	if request.method == "GET":
		form = BookForm()
	else:
		form = BookForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Thank you for submitting the form")

	context = {
		'form': form
	}
	return render(request, 'form.html', context)