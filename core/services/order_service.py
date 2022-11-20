from django.contrib.auth.models import User
from core.models import Order, Stock


class OrderService:
    def buy(user: User, stock: Stock, quantity: int, price: int):
        # # Check if an order position already exists
        # haystack = Order.objects.filter(user=user, price=price, stock=stock)
        #
        # # Look for already existing order positions
        # accumulator = quantity
        # if len(haystack) > 0:
        #     for position in haystack:
        #         if position.action == 1:
        #             #accumulator += position.quantity
        #         else:
        #             accumulator -= position.quantity
        #
        #         if position.action == 0:
        #             position.delete()
        #
        # # If positions eliminate each other
        # if accumulator == 0:
        #     return
        #
        # # Buy = 1, Sell = 0
        # action = 1
        # if accumulator < 0:
        #     action = 0
        #     accumulator = -accumulator
        #
        # # Create new buy-order position
        # order = Order(user=user, price=price, quantity=accumulator, action=action, stock=stock)
        # order.save()

        # # Create new buy-order position
        order = Order(user=user, price=price, quantity=quantity, action=1, stock=stock)
        order.save()

        # Return new order position
        return order

    def sell(user, stock, quantity, price):
        # Create new sell-order position
        order = Order(user=user, price=price, quantity=quantity, action=0, stock=stock)
        order.save()

        # Return new order position
        return order
