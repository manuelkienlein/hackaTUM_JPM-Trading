from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.template import loader

# Create your views here.
#from .models import Book, Author, BookInstance, Genre


def index(request):
    """View function for home page of site."""
    template = loader.get_template('registration/login.html')
    context = {
        'hallo': 10,
    }
    return HttpResponse(template.render(context, request))
#HttpResponse("<h1>Hello World! </h1>")


def registration(request):
    """View function for home page of site."""
    template = loader.get_template('registration.html')
    context = {
        'hallo': 10,

    }
    return HttpResponse(template.render(context, request))
