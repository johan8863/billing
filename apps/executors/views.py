"""executors views"""

# django
from django.urls import reverse_lazy
from django.views import generic

# local
from .models import Executor


class ExecutorList(generic.ListView):
    """Class for listing Executors objects."""
    model = Executor
    paginate_by = 10
    template_name = 'executors/list.html'


class ExecutorCreate(generic.CreateView):
    """Class for creating Executor objects."""
    model = Executor
    fields = [
        "full_name",
        "license_number",
        "personal_id",
    ]
    template_name = 'executors/create_or_update.html'
    success_url = reverse_lazy('executors:list')


class ExecutorUpdate(generic.UpdateView):
    """Class for updating Executors objects."""
    model = Executor
    fields = [
        "full_name",
        "license_number",
        "personal_id",
    ]
    template_name = 'executors/create_or_update.html'
    success_url = reverse_lazy('executors:list')


class ExecutorDelete(generic.DeleteView):
    """Class for deleting Executors objects."""
    model = Executor
    success_url = reverse_lazy('executors:list')