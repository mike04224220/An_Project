# Products Url
from django.urls import path
from .views import ProductFormView, ProductListView, ProductListAPI # Form

urlpatterns = [
    path('lista/', ProductListView.as_view(), name='list_product'),
    path('api/', ProductListAPI.as_view(), name='list_product_api'),
    path('agregar/', ProductFormView.as_view(), name='add_product'),
]