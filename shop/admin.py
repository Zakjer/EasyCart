from django.contrib import admin
from . import models

admin.site.site_header = 'Book shop administration'

class ProductImageInLine(admin.TabularInline):
    model = models.ProductImage
    readonly_fields = ['id', 'product_id']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description', 'price']
    search_fields = ['title', 'description']
    list_editable = ['price']
    ordering = ['title', 'price']
    list_per_page = 30
    inlines = [ProductImageInLine]
    
    def short_description(self, product_instance):
        return product_instance.description[:50]
    

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'phone', 'birth_date'] #DODAC POLE Z MAILEM
    search_fields = ['user']
    list_per_page = 30
    ordering = []

admin.site.register(models.ProductImage)


