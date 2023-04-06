"""kits views"""

# django
from django.urls import reverse_lazy
from django.views import generic

# local
from .models import Kit


class KitList(generic.ListView):
    """class to list kits objects"""
    model = Kit
    paginate_by = 8
    template_name = 'kits/list.html'


class KitUpdate(generic.UpdateView):
    model = Kit
    context_object_name = 'kit'
    fields = ['name']
    template_name = 'kits/update.html'
    success_url = reverse_lazy('kits:list_kits')