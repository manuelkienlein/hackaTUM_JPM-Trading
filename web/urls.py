from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='web_index'),
    path('registration', views.registration, name='web_registration'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts', views.account, name='web_account'),
    path('accounts/orders', views.account_orders, name='web_account_orders'),
    path('accounts/order-history', views.account_order_history, name='web_account_order_history'),
    path('offer/create', views.account_controller_order_create, name = "web_createorder"),
    path('accounts/controller/deleteOrder', views.account_controller_order_delete, name="web_account_controller_order_delete")
]
