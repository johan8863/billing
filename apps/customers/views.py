"""customers views"""

# django
from django.urls import reverse_lazy
from django.views import generic

# local
from .forms import CustomerForm
from .models import Customer


class CustomerList(generic.ListView):
    """Class for listing Customers objects."""
    model = Customer
    paginate_by = 10
    template_name = 'customers/list.html'


class CustomerCreate(generic.CreateView):
    """Class for creating Customers objects"""
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/create_or_update.html'
    success_url = reverse_lazy('customers:list')


class CustomerUpdate(generic.UpdateView):
    """Class for updating Customers objects"""
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/create_or_update.html'
    success_url = reverse_lazy('customers:list')