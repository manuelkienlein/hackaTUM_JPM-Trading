from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:userid>', views.user_index, name='api_user_index'),
]