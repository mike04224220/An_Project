from django.contrib import admin
from .models import Order, OrderProduct  # Models


class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderProduct  # Details => See products
    extra = 0  # No extra lines


class OrderAdmin(admin.ModelAdmin):
    model = Order  # See my order
    inlines = [OrderProductInlineAdmin]  # See products


admin.site.register(Order, OrderAdmin)
