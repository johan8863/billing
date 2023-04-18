"""orders views"""

# django
from django.views import generic

# local
from .models import Order


class OrderList(generic.ListView):
    """Class for listing Orders objects."""
    model = Order
    paginate_by = 10
    template_name = 'orders/list.html'