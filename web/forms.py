from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label='First name', max_length=100)
    last_name = forms.CharField(required=True, label='Last name', max_length=100)
    field_order = ["username", "first_name", "last_name", "email", "password1", "password2"]
