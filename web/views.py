from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

def index(request):
    return redirect('web_login')

def login(request):
    template = loader.get_template('registration/login.html')
    context = {
        'hallo': 10,
    }
    return HttpResponse(template.render(context, request))

def registration(request):
    template = loader.get_template('registration.html')
    context = {
        'hallo': 10,
    }
    return HttpResponse(template.render(context, request))
