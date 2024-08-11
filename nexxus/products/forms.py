from django import forms  # Form
from .models import Product  # Model Product


class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label="Nombre")  # View Client
    description = forms.CharField(max_length=300, label="Descripción")
    priceCost = forms.DecimalField(
        max_digits=10, decimal_places=2, label="Precio Costo"
    )  # 10 numbres / 2 decimals
    priceSell = forms.DecimalField(
        max_digits=10, decimal_places=2, label="Precio Venta"
    )  # 10 numbres / 2 decimals
    available = forms.BooleanField(initial=True, required=False, label="Disponible")
    units = forms.IntegerField(required=False, label="Unidades")

    # Method Validation
    def clean(self):
        cleaned_data = super().clean()
        available = cleaned_data.get("available")
        units = cleaned_data.get("units")

        # Validar que las unidades sean especificadas y no negativas cuando el producto está disponible
        if available and (units is None or units < 1):
            raise forms.ValidationError(
                "Las unidades deben ser especificadas y no negativas cuando el producto está disponible."
            )

        # Validar que no haya unidades disponibles cuando el producto no está disponible
        if not available and units and units > 0:
            raise forms.ValidationError(
                "No puede haber unidades disponibles cuando el producto no está disponible."
            )

        return cleaned_data

    # Method Submit
    def save(self):
        Product.objects.create(
            name=self.cleaned_data["name"],  # Clean Info from customer request
            description=self.cleaned_data["description"],
            priceCost=self.cleaned_data["priceCost"],
            priceSell=self.cleaned_data["priceSell"],
            available=self.cleaned_data["available"],
            units=self.cleaned_data["units"],
        )
