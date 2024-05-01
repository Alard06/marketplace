from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.buyer.views import BuyerRegisterView, BuyerLoginView, logout_view

urlpatterns = [
    path('register/', BuyerRegisterView.as_view(), name='register'),
    path('login/', BuyerLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout')
]
