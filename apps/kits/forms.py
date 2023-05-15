"""kits forms"""

# django
from django import forms

# local
from .models import Kit


class KitForm(forms.ModelForm):
    class Meta:
        model = Kit
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-sm'
            })
        }