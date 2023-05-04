"""orders forms"""

# django
from django import forms

# local
from .models import Order
from ..items.models import Item


class OrderForm(forms.ModelForm):
    """ModelForm Class for Orders objects."""
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'executor_signature_date': forms.DateInput(
                format=('%Y-%m-%d'),
                ),
            'customer_signature_date': forms.DateInput(
                format=('%Y-%m-%d'),
                ),
        }
    # items = forms.ModelMultipleChoiceField(
    #     queryset=Item.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    # )