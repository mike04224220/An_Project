from django.shortcuts import render
from django.views.generic import TemplateView # Home view


class HomeView(TemplateView):
    template_name = 'home.html'  # Nombre de la plantilla
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'WELCOME TO MY WORLD'  # Variable para la plantilla
        return context