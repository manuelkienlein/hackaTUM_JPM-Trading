from django.contrib.auth.models import User

from api.serializers import OrderSerializer, StockSerializer
from core.models import Order, Match, Stock

class MatchingService:
    @staticmethod
    def execute_matching():
        StockSerializer(Stock.objects.all(), many=True)
        orders_json = OrderSerializer(Order.objects.all(), many=True)

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
                        matches.append({"stock": x["stock"], "quantity": y["quantity"], "price_x": x["price"],
                                        "price_y": y["price"], "price_match": y["price"], "id_x": x["id"],
                                        "id_y": y["id"]})
                        book = Match(stock=Stock.objects.get(id=x["stock"]), price_sold=y["price"],
                                     quantity_transaction=y["quantity"], user_buyer=User.objects.get(id=x["user"]),
                                     user_seller=User.objects.get(id=y["user"]))
                        book.save()
                        orders_buy[count]["quantity"] = 0
                        orders_sell[count_y]["quantity"] = 0
                        Order.objects.get(id=x['id']).delete()
                        Order.objects.get(id=y['id']).delete()

                    if x["quantity"] > y["quantity"]:
                        matches.append({"stock": x["stock"], "quantity": y["quantity"], "price_x": x["price"],
                                        "price_y": y["price"], "price_match": y["price"], "id_x": x["id"],
                                        "id_y": y["id"]})
                        orders_buy[count]["quantity"] = orders_buy[count]["quantity"] - orders_sell[count_y]["quantity"]
                        orders_sell[count_y]["quantity"] = 0
                        book = Match(stock=Stock.objects.get(id=x["stock"]), price_sold=y["price"],
                                     quantity_transaction=y["quantity"], user_buyer=User.objects.get(id=x["user"]),
                                     user_seller=User.objects.get(id=y["user"]))
                        book.save()
                        order_x = Order.objects.get(id=x['id'])
                        order_x.quantity -= y["quantity"]
                        order_x.save()
                        order_y = Order.objects.get(id=y['id'])
                        order_y.delete()

                    if x["quantity"] < y["quantity"]:
                        matches.append({"stock": x["stock"], "quantity": y["quantity"], "price_x": x["price"],
                                        "price_y": y["price"], "price_match": y["price"], "id_x": x["id"],
                                        "id_y": y["id"]})
                        book = Match(stock=Stock.objects.get(id=x["stock"]), price_sold=y["price"],
                                     quantity_transaction=x["quantity"], user_buyer=User.objects.get(id=x["user"]),
                                     user_seller=User.objects.get(id=y["user"]))
                        book.save()
                        orders_buy[count]["quantity"] = 0
                        orders_sell[count_y]["quantity"] = orders_sell[count_y]["quantity"] - orders_buy[count][
                            "quantity"]
                        order_y = Order.objects.get(id=y['id'])
                        order_y.quantity -= x["quantity"]
                        order_y.save()
                        order_x = Order.objects.get(id=x['id'])
                        order_x.delete()
        return matches