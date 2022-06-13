from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
import pickle
from .forms import SearchForm


class AboutWebsite(TemplateView):
    template_name = "PhishWebsite/about.html"


class ContactWebsite(TemplateView):
    template_name = "PhishWebsite/contact.html"


class PredictWebsite(TemplateView):
    template_name = "PhishWebsite/predict.html"


class ServiceWebsite(TemplateView):
    template_name = "PhishWebsite/service.html"


class HomeWebsite(TemplateView):
    template_name = "PhishWebsite/index.html"


def ServiceWebsiteView(request):
    prediction_text = ''
    if request.method == "POST":
        predict = SearchForm(data=request.POST)
        if predict.is_valid():
            data = predict.cleaned_data['url']
            print(data)
            model = pickle.load(open('Phishwebsite/phishing.pkl', 'rb'))
            result = model.predict([data])
            if result[0] == "bad":
                prediction_text = "This is a phishing site"
            else:
                prediction_text = "This is not a phishing site"
            return render(request,"Phishwebsite/result.html",{"prediction_text": prediction_text})
        else:
            print(predict.errors)
    else:
        predictForm = SearchForm()
    return render(request, "Phishwebsite/service.html",
                  {"predictForm": predictForm})
