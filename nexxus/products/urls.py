# Products Url
from django.urls import path
from .views import ProductFormView # Form

urlpatterns = [
    path('agregar/', ProductFormView.as_view(), name="add_product"),
]