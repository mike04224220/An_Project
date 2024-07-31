from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic # class
from .forms import ProductForm # form
from django.urls import reverse_lazy # success_url



class ProductFormView(generic.FormView):
    template_name = "add_product.html" # Name Html
    form_class = ProductForm # form
    success_url = reverse_lazy('add_product') # Redirect after created

    def form_valid(self, form): # Recept form and save
        form.save()
        return super().form_valid(form)