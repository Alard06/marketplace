
from django.urls import path, include

from apps.product.views import categories_list, card_subcategory

urlpatterns = [
    path('categories/', categories_list, name='category'),
    path('categories/<str:slug>/', card_subcategory, name='card_subcategory')
]
