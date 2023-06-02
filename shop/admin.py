from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
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
    list_per_page = 20
    inlines = [ProductImageInLine]
    
    def short_description(self, product_instance):
        return product_instance.description[:50]
    

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'birth_date']
    search_fields = ['user']
    list_per_page = 20


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    ordering = ['username', 'first_name', 'last_name']
    list_per_page = 20
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email", "first_name", "last_name"),
            },
        ),
    )


class OrderItemInLine(admin.TabularInline):
    model = models.OrderItem
    readonly_fields = ['product_name', 'quantity', 'price']
    autocomplete_fields = ['product']
    exclude = ['product']

    def product_name(self, orderitem):
        return orderitem.product.title
    

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInLine]

    def get_total_price(self, obj):
        total = sum(item.price for item in obj.orderitem_set.all())
        return total
    

admin.site.register(models.ProductImage)


