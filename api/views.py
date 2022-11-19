from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def user_index(request, userid):
    return HttpResponse("TODO: API UserId " + str(userid))

def user_stocks(request, userid):
    return HttpResponse("TODO: API UserId " + str(userid))

def user_stocks_buy(request, userid):
    return HttpResponse("TODO: API UserId " + str(userid))

def user_stocks_sell(request, userid):
    return HttpResponse("TODO: API UserId " + str(userid))

def user_stocks_delete(request, userid):
    return HttpResponse("TODO: API UserId " + str(userid))


def stocks_index(request):
    return HttpResponse("TODO: API Stocks Listing")
def stocks_info(request, stockId):
    return HttpResponse("TODO: API Stocks Info " + str(stockId))
