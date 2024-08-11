from django.db import models  # Default
from django.contrib.auth.models import User  # Model => Foreign User
from products.models import Product  # Model => Foreign product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Delete all order
    is_active = models.BooleanField(default=True)  # is ther order active ?
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"order {self.id} by {self.user}"  # orderID by userID


class OrderProduct(models.Model):  # Save products
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # Delete all order
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT
    )  # Only delete product
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.order} - {self.product}"
