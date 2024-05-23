# Register your models here.
from django.contrib import admin

from orders.models import Order, OrderItem


# admin.site.register(Order)
# admin.site.register(OrderItem)

class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = "product", "name", "price", "quantity", "options",
    search_fields = (
        "product",
        "name",
    )
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = "order", "product", "name", "price", "quantity",
    search_fields = (
        "order",
        "product",
        "name",
    )


class OrderTabulareAdmin(admin.TabularInline):
    model = Order
    fields = (
        "requires_delivery",
        "status",

        "is_paid",
        "created_timestamp",
    )

    search_fields = (
        "requires_delivery",
        "is_paid",
        "created_timestamp",
    )
    readonly_fields = ("created_timestamp",)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        "id",
        "user",
        "requires_delivery",
        "status",
        "is_paid",
        "created_timestamp",
        'status'
    )


    search_fields = (
        "id",
    )
    readonly_fields = ("created_timestamp",)
    list_filter = (
        "requires_delivery",
        "status",
        "is_paid",
    )
    inlines = (OrderItemTabulareAdmin,)
