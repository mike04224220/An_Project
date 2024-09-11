from django.contrib import admin
from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):  # Create / Register Models
    model = Product
    list_display = ["name", "priceSell"]  # See Fields
    search_fields = ["name"]  # Filter and Search


admin.site.register(Product, ProductAdmin)  # Model and Class
