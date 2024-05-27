from django.contrib import admin
from orders.models import Order, OrderItem


class OrderItemTabulareAdmin(admin.TabularInline):
    """
    Класс OrderItemAdmin — это представление содержания заказа в интерфейсе админ-понели
    """
    model = OrderItem
    fields = "product", "name", "price", "quantity", "options"
    search_fields = (
        "product",
        "name",
    )
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """
    Класс OrderItemAdmin — это представление заказа в интерфейсе админ-понели
    """

    list_display = "order", "product", "name", "price", "quantity",
    search_fields = (
        "order",
        "product",
        "name",
    )


class OrderTabulareAdmin(admin.TabularInline):
    """
    Класс OrderTabulareAdmin — это представление полей и навигации в интерфейсе админ-понели
    """
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
    """
    Класс OrderAdmin — это представление модели в интерфейсе админ-понели.
    """
    list_display = (
        '__str__',
        "id",
        "user",
        "requires_delivery",
        "status",
        "is_paid",
        "created_timestamp",
        'status',
        'time_pickup_delivery',
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
