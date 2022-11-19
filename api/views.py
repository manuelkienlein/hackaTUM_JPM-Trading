from django.core import serializers
from django.http import HttpResponse, JsonResponse

from api.serializers import ModelSerializer
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

@api_view(['GET'])
def stocks_index(request):
    serializer = ModelSerializer(Stock.objects.all(), many=True)
    return Response(serializer.data)

@api_view(['GET'])
def stocks_info(request, stockId):
    serializer = ModelSerializer(Stock.objects.get(id=stockId), many=False)
    return Response(serializer.data)
