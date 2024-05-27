from django.contrib import admin

from cart.models import Cart, Coupon


class CartTabAdmin(admin.TabularInline):
    """
    Класс CartTabAdmin — это представление корзины в интерфейсе админ-панели
    """
    model = Cart
    fields = "product", "quantity", "created_timestamp", "options", "final_price"
    search_fields = "product", "quantity", "created_timestamp"
    readonly_fields = ("created_timestamp",)
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """
    Класс CartAdmin — это представление модели Карты в интерфейсе админ-панели.
    """
    list_display = ["user_display", "product_display", "created_timestamp", 'quantity']
    list_filter = ["created_timestamp", "user", "product__name",]

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонимный пользователь"

    def product_display(self, obj):
        return str(obj.product.name)

@admin.register(Coupon)
class UserAdmin(admin.ModelAdmin):
    """
    Класс UserAdmin — это представление модели Купонов в интерфейсе админ-панели.
    """
    list_display = ['code', 'valid_from', 'valid_to', 'discount', 'active']
    search_fields = ['code',]
    list_editable = ['active']
