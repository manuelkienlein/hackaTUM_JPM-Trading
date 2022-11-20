from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import F, Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from core.models import Order, Stock, Match
from core.services.order_service import OrderService
from web.forms import RegisterUserForm, CreateOrderForm, DeleteOrderForm


def index(request):
    return redirect('login')


def login(request):
    template = loader.get_template('registration/login.html')
    return HttpResponse(template.render({}, request))


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
            return redirect("web_account")
    form = RegisterUserForm()
    context = {
        'register_form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def account(request):
    # Time is money and since this is a hackathon, we will save time by not writing complex and efficient sql queries.

    stocks = {}
    names = {}
    for stock in Stock.objects.all():
        stocks[stock.wkn] = 0
        names[stock.wkn] = stock.name

    for transaction in Match.objects.filter(Q(user_buyer=request.user) | Q(user_seller=request.user)):
        if (transaction.user_buyer == request.user):
            stocks[transaction.stock.wkn] = stocks[transaction.stock.wkn] + transaction.quantity_transaction
        else:
            stocks[transaction.stock.wkn] = stocks[transaction.stock.wkn] - transaction.quantity_transaction

    catalog = []
    for wkn in stocks.keys():
        catalog.append({"wkn": wkn, "name": names[wkn], "quantity": stocks[wkn]})

    return render(request, 'account/account.html', {'stocks': catalog})


def account_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'account/orders.html', {'orders': orders})


def account_order_history(request):
    matches = Match.objects.filter(Q(user_buyer=request.user) | Q(user_seller=request.user))
    return render(request, 'account/order-history.html', {'matches': matches})


def account_controller_order_create(request):
    if request.POST:
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            user = request.user
            stock = form.cleaned_data['stock']
            quantity = form.cleaned_data['quantity']
            price = form.cleaned_data['price']
            if form.cleaned_data['action'] == '1':
                OrderService.buy(user, stock, quantity, price)
            else:
                OrderService.sell(user, stock, quantity, price)
    form = CreateOrderForm()
    return render(request, "create.html", {"form": form})


def account_controller_order_delete(request):
    order = Order.objects.get(id=request.GET.get('id'))
    OrderService.delete(order)
    return redirect('web_account_orders')
