from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic  # class
from .forms import ProductForm  # form
from django.urls import reverse_lazy  # success_url
from .models import Product

from rest_framework.views import APIView  # Framework
from .serializers import ProductSerializer
from rest_framework.response import Response


class ProductFormView(generic.FormView):
    template_name = "add_product.html"  # Name Html
    form_class = ProductForm  # form
    success_url = reverse_lazy("add_product")  # Redirect after created

    def form_valid(self, form):  # Recept form and save
        form.save()
        return super().form_valid(form)


class ProductListView(generic.ListView):
    model = Product
    template_name = "list_product.html"
    context_object_name = "products"


class ProductListAPI(APIView):
    authentication_classes = []  # Remove authentication
    permission_classes = []  # Remove permissions

    def get(self, request):  # Json => Al products
        products = Product.objects.all()
        # Many=True=> List
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)  # Json Data
