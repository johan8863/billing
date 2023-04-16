"""customers forms"""

# django
from django import forms

# local
from .models import Customer


class CustomerForm(forms.ModelForm):
    """Class to link Customer model with django ModelForm Class"""
    class Meta:
        model = Customer
        fields = [
            "customer_type",
            "name",
            "address",
            "province",
            "township",
            "code",
            "client_nit",
            "bank_account_header",
            "bank_account",
        ]