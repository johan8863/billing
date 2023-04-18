"""orders forms"""

# django
from django import forms

# local
from .models import Order


class OrderForm(forms.ModelForm):
    """ModelForm Class for Orders objects."""
    class Meta:
        model = Order
        exclude = [
            'is_active',
        ]
        widgets = {
            'executor_signature_date': forms.DateInput(
                format=('%Y-%m-%d'),
                ),
            'customer_signature_date': forms.DateInput(
                format=('%Y-%m-%d'),
                ),
        }