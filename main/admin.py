from django.contrib import admin
from main.models import Category, Products

@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated')
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Products)
class ProductssAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated', 'available')
    prepopulated_fields = {'slug': ('name', )}

