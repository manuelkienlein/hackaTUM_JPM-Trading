from django.contrib.auth.models import User
from api.serializers import StockSerializer, OrderSerializer, UserSerializer
from core.models import Stock, Order
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.services.matching_service import MatchingService
from core.services.order_service import OrderService


@api_view(['GET'])
def users_index(request):
    serializer = UserSerializer(User.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def users_info(request, userId):
    serializer = UserSerializer(User.objects.get(id=userId), many=False)
    return Response(serializer.data)


@api_view(['GET'])
def users_stocks_buy(request, userId):
    stock = Stock.objects.filter(wkn=request.GET.get('stock'))[0]
    quantity = request.GET.get('quantity')
    price = request.GET.get('price')

    order = OrderService.buy(request.user, stock, quantity, price)
    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def users_stocks_sell(request, userId):
    stock = Stock.objects.filter(wkn=request.GET.get('stock'))[0]
    quantity = request.GET.get('quantity')
    price = request.GET.get('price')

    order = OrderService.sell(request.user, stock, quantity, price)
    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def users_stocks_delete(request, userId):
    order = Order.objects.get(id=request.GET.get('orderId'))
    OrderService.delete(order)
    data = {
        'message': 'Deleted order successfully!',
    }
    return Response(data)


@api_view(['GET'])
def users_orders_index(request, userId):
    user = User.objects.get(id=userId)
    serializer = OrderSerializer(Order.objects.filter(user=user), many=True)
    return Response(serializer.data)


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


@api_view(['GET'])
def orders_matching(request):
    matches = MatchingService.execute_matching()
    data = {
        'message': 'Order matching job completed successfully',
        'matchesCount': len(matches),
        'matches': matches
    }
    return Response(data)
