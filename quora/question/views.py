from django.shortcuts import render
from django.http import HttpResponse

import pprint

# Create your views here.

def welcome(request):
	print('-+'*20)
	print("Request receieved at welcome")
	print('User: ', request.user)
	print('Is AJAX: ', request.is_ajax())
	print('Method: ', request.method)
	print('-+'*20)
	return render(request, 'welcome.html')
#	return HttpResponse('asdfasdfasdfasdfasdf')

def abc(request):
	print('-+'*20)
	print("Request received at abc")
	print('-+'*20)
	context = {'username': 'Django', 'num': 207}
	return render(request, 'abc.html', context)
