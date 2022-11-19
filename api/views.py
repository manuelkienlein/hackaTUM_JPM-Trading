from django.core import serializers
from django.http import HttpResponse, JsonResponse
from core.models import Stock
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
    return HttpResponse(serializers.serialize('json', Stock.objects.all()), content_type="text/json")
def stocks_info(request, stockId):
    return HttpResponse("TODO: API Stocks Info " + str(stockId))


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
    return Response(api_urls)
