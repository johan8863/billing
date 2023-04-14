"""executors views"""

# django
from django.views import generic

# local
from .models import Executor


class ExecutorList(generic.ListView):
    """Class for listing Executors objects."""
    model = Executor
    paginate_by = 10
    template_name = 'executors/list.html'