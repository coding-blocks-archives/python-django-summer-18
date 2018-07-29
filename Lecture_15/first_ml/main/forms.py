from django import forms

class MLForm(forms.Form):
    input_string = forms.CharField(max_length=100)