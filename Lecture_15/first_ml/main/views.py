from django.shortcuts import render
from django.views.generic import View

from . import forms

from . import sentiments

# Create your views here.

class Index(View):
    def get(self, request):
        form = forms.MLForm()

        context = {
            "form": form
        }
        return render(request, 'main/index.html', context)

    def post(self, request):
        form = forms.MLForm(request.POST)
        output = ''
        if form.is_valid():
            input_string = form.cleaned_data['input_string']

            # Apply ML
            output_dict = sentiments.classify_sentiment(input_string)

            output = "Positive: {}% and Negative: {}%".format(output_dict['pos']*100, output_dict['neg']*100)

            form = forms.MLForm()

        context = {
            "form": form,
            "output": output
        }
        return render(request, 'main/index.html', context)
        