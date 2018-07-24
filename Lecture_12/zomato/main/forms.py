from django import forms

from . import models

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget = forms.PasswordInput())

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = models.Restaurant
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        exclude = ['restaurant',]