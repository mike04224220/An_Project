# Detail => Model's specific object --- Create =>
from django.views.generic import DetailView, CreateView  # Detail
from django.contrib.auth.mixins import LoginRequiredMixin  # When user's logged
from django.urls import reverse_lazy  # Return

from .models import Order  # Model
from .forms import OrderProductForm  # Form


class MyOrderView(LoginRequiredMixin, DetailView):  # User logged, detaisView
    model = Order
    template_name = "my_order.html"
    context_object_name = "order"  # Name context bar => Base html

    def get_object(self, queryset=None):  # From ccbv.co.uk
        return Order.objects.filter(
            is_active=True,  # Actives
            user=self.request.user,  # Filter User => Same user
        ).first()  # An Active Order - first => 1 Object


class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = "create_order_product.html"  # Template
    form_class = OrderProductForm  # My form
    success_url = reverse_lazy("my_order")  # After => Url to go

    def form_valid(self, form):  # Is teh form valid
        # order, boolean (created)
        order, _ = Order.objects.get_or_create(  # get or create
            is_active=True,  # Only one order by user
            user=self.request.user,  # Filter User => Same user
        )
        form.instance.order = order  # Instance
        form.instance.quantity = 1  # 1 product
        form.save()  # Save on database
        return super().form_valid(form)  # Call Functions
