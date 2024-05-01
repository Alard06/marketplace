
from django.urls import path

from apps.buyer.views import register

urlpatterns = [
    path('register/', register, name='register'),
]
