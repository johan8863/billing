"""items views"""

# django
from django.views import generic

# local
from .models import Item


class ItemList(generic.ListView):
    """Class for listing Item objects"""
    model = Item
    paginate_by = 10
    template_name = 'items/list.html'