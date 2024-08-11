from django.forms import ModelForm # Model form
from .models import OrderProduct # Model same folder

# Model Form => Without copy field form model, only bring model's fields
class OrderProductForm(ModelForm): 
    class Meta: # Requirement
        model = OrderProduct
        fields = ["product"] # List => Product