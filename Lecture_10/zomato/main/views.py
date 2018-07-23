from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg

from . import models
from . import forms

# Create your views here.

def index(request):
    context = {}
    return render(request, 'main/index.html', context)

def restaurants(request):
    query_set = models.Restaurant.objects.all()

    query_set = query_set.annotate(average_rating = Avg('review__rating')).order_by('-average_rating')

    context = {
        "query_set": query_set,
    }
    return render(request, 'main/restaurants.html', context)

def add_restraunt(request):
    if request.method == "GET":
        form = forms.RestaurantForm()
    else: # POST request
        form = forms.RestaurantForm(request.POST)

        if form.is_valid():
            obj = form.save()
            return HttpResponse("Form Added with id " + str(obj.pk))

    context = {
        'rest_form': form
    }
    return render(request, 'main/addRestaurant.html', context)

def restaurant(request, id):
    rest = get_object_or_404(models.Restaurant, pk = id)

    # try:
    #     rest = models.Restaurant.objects.get(pk = id)
    # except:
    #     raise Http404()
    
    
    success = False

    # Handling the form
    if request.method == "GET":
        form = forms.ReviewForm()
    else:
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            obj = form.save(commit = False)
            obj.restaurant = rest
            obj.save()

            success = True
            form = forms.ReviewForm()

    context = {
        'restaurant': rest,
        'form': form,
        'success': success
    }
    return render(request, 'main/restaurant.html', context)

def review(request, id):
    obj = get_object_or_404(models.Review, pk = id)

    context = {
        'review': obj
    }
    return render(request, 'main/review.html', context)