from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from api.serializers import OrderSerializer
from core.models import Order, Stock, Match
from api.forms import orderData, deleteOrder
from web.forms import RegisterUserForm
from django.db.models import F, Q


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
    return render(request, 'account/account.html', {'foo': 'bar'})


def account_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'account/orders.html', {'orders': orders})


def account_order_history(request):
    matches = Match.objects.filter(Q(user_buyer=request.user) | Q(user_seller=request.user))
    return render(request, 'account/order-history.html', {'matches': matches})

def create(request):
    form = orderData(request.POST)
    if request.POST:
        if form.is_valid():
            if request.POST.get('action') == "on":
                actionBool = True
            else:
                actionBool = False
            createOrder = Order(user_id=request.POST.get('userForm'), price=request.POST.get(
                'price'), quantity=request.POST.get('quantity'), action=actionBool, stock=Stock.objects.get(id=1))
            createOrder.save()
    return render(request, "create.html", {"form": form})


def delete(request):
    form = deleteOrder(request.POST)
    if request.POST:
        if form.is_valid():
            quantity = request.POST.get("quantity")
            stockID = request.POST.get("stock")
            userInformation = Order.objects.filter(order = Order.getrequest.order)
            if quantity < int(userInformation.values("quantity")[0]["quantity"]):
                userInformation.update(quantity=F('quantity')-quantity)

    return render(request, "delete.html", {"form": form})
            #command hallo
