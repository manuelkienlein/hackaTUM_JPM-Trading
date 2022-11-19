from django.urls import path, include
from . import views


urlpatterns = [
    path('login', views.index, name='web_index'),
    path('registration', views.registration, name='web_registration'),
]
