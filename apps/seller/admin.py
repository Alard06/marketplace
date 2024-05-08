from django.contrib import admin

from apps.seller.models import SellerApplication


@admin.register(SellerApplication)
class SellerApplicationAdmin(admin.ModelAdmin):
    pass