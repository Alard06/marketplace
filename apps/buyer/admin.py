from django.contrib import admin

from apps.buyer.models import Buyer


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'bonus', 'email', 'telephone', )