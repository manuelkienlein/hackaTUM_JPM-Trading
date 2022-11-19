from django.urls import path, include
from . import views
from api.views import create
urlpatterns = [
    path('login', views.index, name='web_index'),
    path('registration', views.registration, name='web_registration'),
    path('offer/create', create, name = "web_createorder"),
]
