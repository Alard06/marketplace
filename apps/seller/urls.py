from django.urls import path

from apps.buyer.views import BuyerRegisterView
from apps.main.views import index
from apps.seller.views import seller_index, seller_register, seller_profile

urlpatterns = [
    path('sellers/', seller_index, name='seller_index'),
    path('sellers/register', seller_register, name='seller_register'),
    path('seller/profile', seller_profile, name='seller_profile')
]
