# Products Url
from django.urls import path
from .views import ProductFormView, ProductListView # Form

urlpatterns = [
    path('lista/', ProductListView.as_view(), name='list_product'),
    path('agregar/', ProductFormView.as_view(), name="add_product"),
]