from django.urls import path
from .views import HomeView # Form

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]