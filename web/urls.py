from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='web_index'),
    path('login', views.login, name='web_login'),
    path('registration', views.registration, name='web_registration'),
]
