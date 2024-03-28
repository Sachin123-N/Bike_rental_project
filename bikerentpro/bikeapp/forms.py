from django import forms
from .models import Bike


class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = "__all__"

        widgets = {
            "bike_rental_name": forms.TextInput(attrs={'class': 'class-controls'}),
            "hour_price": forms.NumberInput(attrs={'class': 'class-controls'}),
            "total_rental_time": forms.NumberInput(attrs={'class': 'class-controls'}),
            "discount_price": forms.NumberInput(attrs={'class': 'class-controls'}),
            "payment_mode": forms.Select(attrs={'class': 'class-controls'}),
            "bike_quantity": forms.Select(attrs={'class': 'class-controls'}),
        }
