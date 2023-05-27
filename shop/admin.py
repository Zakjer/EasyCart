from django.contrib import admin
from . import models

admin.site.site_header = 'Book shop administration'

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description', 'price']
    search_fields = ['title', 'description']
    list_editable = ['price']
    ordering = ['title', 'price']
    list_per_page = 30
    
    def short_description(self, product_instance):
        return product_instance.description[:50]


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'phone', 'birth_date', 'email']
    search_fields = ['user', 'email']
    list_per_page = 30
    ordering = []


