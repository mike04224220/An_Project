from django.urls import path
from django.contrib.auth.views import LoginView # View Login
# from .views import 

urlpatterns = [
    path(
        'login/', 
        LoginView.as_view(template_name='login.html'), 
        name='login'
    ),
]