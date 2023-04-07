"""kits views"""

# django
from django.urls import reverse_lazy
from django.views import generic

# local
from .models import Kit


class KitList(generic.ListView):
    """class for listing kits objects"""
    model = Kit
    paginate_by = 8
    template_name = 'kits/list.html'


class KitCreate(generic.CreateView):
    """Class for creating Kit objects"""
    model = Kit
    fields = ['name']
    template_name = 'kits/create.html'
    success_url = reverse_lazy('kits:list_kits')


class KitUpdate(generic.UpdateView):
    """Class for updating Kit objects"""
    model = Kit
    context_object_name = 'kit'
    fields = ['name']
    template_name = 'kits/update.html'
    success_url = reverse_lazy('kits:list_kits')