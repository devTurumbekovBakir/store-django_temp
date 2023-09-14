from django.contrib import admin

from .models import ProductCategory, Product, Basket


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category']
    fields = ['image', 'name', 'description', ('price', 'quantity'), 'category']
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name', 'description']
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ['product', 'quantity']
    readonly_fields = ('created_timestamp',)
    extra = 0
