
from django.urls import path, include

from apps.product.views import categories_list, card_subcategory, product_list, view_cart, add_to_cart, remove_from_cart

urlpatterns = [
    path('categories/', categories_list, name='category'),
    path('categories/<str:slug>/', card_subcategory, name='card_subcategory'),
    path('product/<str:slug>', product_list, name='product_list'),
    path('cart/', view_cart, name='view_cart'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
]
