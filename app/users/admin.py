from django.contrib import admin, messages
from django.core.exceptions import ValidationError

from app.users.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_admin', 'is_superuser', 'is_active', 'created_at', 'updated_at')