from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader

from web.forms import RegisterUserForm


def index(request):
    return redirect('login')

def login(request):
    template = loader.get_template('registration/login.html')
    context = {
        'hallo': 10,
    }
    return HttpResponse(template.render(context, request))

def registration(request):
    template = loader.get_template('registration.html')
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            instance = form.save()  # form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = request.POST.get('email')  # getting email
            first_name = request.POST.get('first_name')  # getting first name
            last_name = request.POST.get('last_name')  # getting last name
            user = authenticate(username=username, password=password)  # making user
            instance.email = email  # saving email
            instance.first_name = first_name  # saving email
            instance.last_name = last_name  # saving email
            instance.save()  # save form
            form.save_m2m()  # save all
            #messages.success(request, "Registration successful.")
            return redirect("web_account")
        #messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterUserForm()
    context = {
        'register_form': form,
    }
    return HttpResponse(template.render(context, request))

def account(request):
    return render(request, 'account.html', {'foo': 'bar'})