from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:userid>', views.user_index, name='api_user_index'),
    path('user/<int:userid>/stocks', views.user_stocks, name='api_user_info'),
    path('user/<int:userid>/stocks/buy', views.user_stocks_buy, name='api_user_stocks_buy'),
    path('user/<int:userid>/stocks/sell', views.user_stocks_buy, name='api_user_stocks_sell'),
    path('user/<int:userid>/stocks/delete', views.user_stocks_delete, name='api_user_stocks_delete'),

    path('orders', views.orders_index, name='orders_index'),
    path('orders/<int:orderId>', views.orders_info, name='orders_info'),

    path('stocks', views.stocks_index, name='stocks_index'),
    path('stocks/matching', views.orders_matching, name='orders_matching'),
    path('stocks/<int:stockId>', views.stocks_info, name='stocks_info'),
]
