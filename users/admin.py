from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin

from cart.admin import CartTabAdmin

admin.site.register(User)


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email",]
    search_fields = ["username", "first_name", "last_name", "email",]
    inlines = [CartTabAdmin, ]

AUTH_USER_MODEL = 'users.User'
