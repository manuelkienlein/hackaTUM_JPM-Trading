from django.http import HttpResponse

from api.serializers import StockSerializer, OrderSerializer
from core.models import Stock, Order
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

@api_view(['GET'])
def orders_index(request):
    serializer = OrderSerializer(Order.objects.all(), many=True)
    return Response(serializer.data)

@api_view(['GET'])
def orders_info(request, orderId):
    serializer = OrderSerializer(Order.objects.get(id=orderId), many=False)
    return Response(serializer.data)

@api_view(['GET'])
def stocks_index(request):
    serializer = StockSerializer(Stock.objects.all(), many=True)
    return Response(serializer.data)

@api_view(['GET'])
def stocks_info(request, stockId):
    serializer = StockSerializer(Stock.objects.get(id=stockId), many=False)
    return Response(serializer.data)
