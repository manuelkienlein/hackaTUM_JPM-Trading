from django import forms
from core.models import Order, Stock, User


class orderData(forms.Form):

    stock = forms.ModelChoiceField(queryset=Stock.objects.all())
    userForm = forms.ModelChoiceField(queryset=User.objects.all())
    price = forms.CharField(label = "Stock Price")
    quantity = forms.CharField(label = "Quantity")
    action = forms.BooleanField(required=False, label = "Action")


class deleteOrder(forms.Form):

    stock = forms.ModelChoiceField(queryset=Stock.objects.all())
    userForm = forms.ModelChoiceField(queryset=User.objects.all())
    quantity = forms.IntegerField(label = "Quantity")
