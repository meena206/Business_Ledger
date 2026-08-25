from django.contrib import admin
from .models import Customer, Transaction

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "phone",
        "city",
        "owner",
        "created_at"
    )

    search_fields = (
        "name",
        "phone",
        "email",
        "city"
    )

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):

    list_display = (
        "customer",
        "transaction_type",
        "amount",
        "date"
    )

    list_filter = (
        "transaction_type",
        "date"
    )

    search_fields = (
        "customer__name",
        "description"
    )