"""items views"""

# django
from django.urls import reverse_lazy
from django.views import generic

# local
from .models import Item


class ItemList(generic.ListView):
    """Class for listing Item objects"""
    model = Item
    paginate_by = 10
    template_name = 'items/list.html'


class ItemCreate(generic.CreateView):
    """Class for creating Item objects"""
    model = Item
    fields = [
        "code",
        "name",
        "item_type",
        "price",
        "measurement"
    ]
    template_name = 'items/create.html'
    success_url = reverse_lazy('items:list')