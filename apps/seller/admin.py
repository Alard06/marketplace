from django.contrib import admin

from apps.seller.models import Seller


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
