from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import Stock


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label='First name', max_length=100)
    last_name = forms.CharField(required=True, label='Last name', max_length=100)
    field_order = ["username", "first_name", "last_name", "email", "password1", "password2"]


class CreateOrderForm(forms.Form):
    stock = forms.ModelChoiceField(required=True, queryset=Stock.objects.all())
    price = forms.IntegerField(required=True, label="Stock Price")
    quantity = forms.IntegerField(required=True, label="Quantity")
    action = forms.ChoiceField(choices=[('1', 'Buy stock'), ('0', 'Sell stock')], label="Action",
                               initial='1', widget=forms.Select(), required=False)


class DeleteOrderForm(forms.Form):
    stock = forms.ModelChoiceField(queryset=Stock.objects.all())
    quantity = forms.IntegerField(label="Quantity")
