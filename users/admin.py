from django.contrib import admin
from users.models import User
from cart.admin import CartTabAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["__str__", "username", "first_name", "last_name", "email", ]
    search_fields = ["username", "first_name", "last_name", "email", ]
    inlines = [CartTabAdmin, ]


AUTH_USER_MODEL = 'users.User'
