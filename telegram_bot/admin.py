from django.contrib import admin

from telegram_bot.models import Owner


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'role', 'telegram_id']
