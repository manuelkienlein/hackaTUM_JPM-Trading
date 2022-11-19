from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='web_index'),
    path('registration', views.registration, name='web_registration'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts', views.account, name='web_account'),
]
