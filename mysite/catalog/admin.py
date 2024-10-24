from django.contrib import admin
from .models import Product, Category, Version
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'category', 'image', 'description', 'publicate', 'slug']
    filter = ['category']
    search_fields = ['name', 'price']
    list_display = ['name', 'price', 'category', 'id', 'slug']


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name', 'id']


class VersionAdmin(admin.ModelAdmin):
    field = ['product', 'version_name', 'version_number', 'is_current']
    list_display = ['product', 'version_name', 'version_number', 'is_current']


admin.site.register(Version, VersionAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
