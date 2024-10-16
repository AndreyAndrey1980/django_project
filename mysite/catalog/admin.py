from django.contrib import admin
from .models import Product, Category
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'category', 'image', 'description']
    filter = ['category']
    search_fields = ['name', 'price']
    list_display = ['name', 'price', 'category', 'id']


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name', 'id']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
