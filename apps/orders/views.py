"""orders views"""

# django
from django.urls import reverse_lazy
from django.views import generic

# local
from .forms import OrderForm
from .models import Order


class OrderList(generic.ListView):
    """Class for listing Orders objects."""
    model = Order
    paginate_by = 10
    template_name = 'orders/list.html'


class OrderCreate(generic.CreateView):
    """Class for creating Orders objects."""
    model = Order
    form_class = OrderForm
    template_name = 'orders/create_or_update.html'
    success_url = reverse_lazy('orders:list')