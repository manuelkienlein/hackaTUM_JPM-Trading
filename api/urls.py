from django.urls import path
from . import views

urlpatterns = [
    path('users', views.users_index, name='api_user_index'),
    path('users/<int:userId>', views.users_info, name='api_user_index'),
    path('users/<int:userId>/stocks/buy', views.users_stocks_buy, name='api_user_stocks_buy'),
    path('users/<int:userId>/stocks/sell', views.users_stocks_sell, name='api_user_stocks_sell'),
    path('users/<int:userId>/stocks/delete', views.users_stocks_delete, name='api_user_stocks_delete'),
    path('users/<int:userId>/orders', views.users_orders_index, name='api_user_orders_index'),

    path('orders', views.orders_index, name='orders_index'),
    path('orders/<int:orderId>', views.orders_info, name='orders_info'),
    path('stocks', views.stocks_index, name='stocks_index'),
    path('stocks/matching', views.orders_matching, name='orders_matching'),
    path('stocks/<int:stockId>', views.stocks_info, name='stocks_info'),
]
