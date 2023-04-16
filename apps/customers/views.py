"""customers views"""

# django
from django.views import generic

# local
from .models import Customer


class CustomerList(generic.ListView):
    """Class for listing Customers objects."""
    model = Customer
    paginate_by = 10
    template_name = 'customers/list.html'