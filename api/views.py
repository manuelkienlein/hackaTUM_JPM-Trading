from django.contrib.auth.models import User
from django.http import HttpResponse
from api.serializers import StockSerializer, OrderSerializer, UserSerializer
from core.models import Stock, Order, Match
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
def users_stocks(request, userId):
    # TODO
    return HttpResponse("TODO: API UserId " + str(userId))


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
    # TODO
    return HttpResponse("TODO: API UserId " + str(userId))


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
    serializer = StockSerializer(Stock.objects.all(), many=True)
    orders_json = OrderSerializer(Order.objects.all(), many=True)

    stock_names = []
    orders_sell = []
    orders_buy = []
    matches = []

    for n in orders_json.data:
        if not n["action"]:
            orders_buy.append(n)
        if n["action"]:
            orders_sell.append(n)

    for count, x in enumerate(orders_buy):
        for count_y, y in enumerate(orders_sell):
            if x["price"] >= y["price"] and x["stock"] == y["stock"] and x["quantity"] > 0 and y["quantity"] > 0:

                if x["quantity"] == y["quantity"]:
                    #matches.append(matches.append({"stock": x["stock"], "quantity": y["quantity"], "price_x": x["price"], "price_y": y["price"], "price_match": y["price"], "id_x": x["id"], "id_y":y["id"]}))
                    book = Match(stock=x["stock"], price_sold=y["price"], quantity_transaction=y["quantity"], user_buyer=User.objects.get(id=x["id"]), user_seller=User.objects.get(id=y["id"]))
                    book.save()
                    orders_buy[count]["quantity"] = 0
                    orders_sell[count_y]["quantity"] = 0


                if x["quantity"] > y["quantity"]:
                    #matches.append(matches.append({"stock": x["stock"], "quantity": y["quantity"], "price_x": x["price"], "price_y": y["price"], "price_match": y["price"], "id_x": x["id"], "id_y":y["id"]}))
                    orders_buy[count]["quantity"] = orders_buy[count]["quantity"] - orders_sell[count_y]["quantity"]
                    orders_sell[count_y]["quantity"] = 0
                    book = Match(stock=x["stock"], price_sold=y["price"], quantity_transaction=y["quantity"], user_buyer=User.objects.get(id=x["user"]), user_seller=User.objects.get(id=y["user"]))
                    book.save()


                if x["quantity"] < y["quantity"]:
                    #matches.append(matches.append({"stock": x["stock"], "quantity": y["quantity"], "price_x": x["price"], "price_y": y["price"], "price_match": y["price"], "id_x": x["id"], "id_y":y["id"]}))
                    book = Match(stock=x["stock"], price_sold=y["price"], quantity_transaction=x["quantity"], user_buyer=User.objects.get(id=x["user"]), user_seller=User.objects.get(id=y["user"]))
                    book.save()
                    orders_buy[count]["quantity"] = 0
                    orders_sell[count_y]["quantity"] = orders_sell[count_y]["quantity"] - orders_buy[count]["quantity"]


    return Response([orders_buy, orders_sell, matches])
