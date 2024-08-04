from django.urls import path
from .views import HomeView # Form

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
]