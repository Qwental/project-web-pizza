from django.contrib import admin
from main.models import Addition, Category, Products, SpecialOffers


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductssAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated', 'available', 'discount')
    list_editable = ['discount', 'available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    list_filter = ['category', ]


@admin.register(Addition)
class AdditionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(SpecialOffers)
class SpecialOffersAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated')
