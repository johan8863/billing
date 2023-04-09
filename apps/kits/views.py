"""kits views"""

# django
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

# local
from .models import Kit


class KitList(generic.ListView):
    """class for listing kits objects"""
    model = Kit
    paginate_by = 10
    template_name = 'kits/list.html'


class KitCreate(generic.CreateView):
    """Class for creating Kit objects"""
    model = Kit
    fields = ['name']
    template_name = 'kits/create_or_update.html'
    success_url = reverse_lazy('kits:list')


class KitUpdate(generic.UpdateView):
    """Class for updating Kit objects"""
    model = Kit
    context_object_name = 'kit'
    fields = ['name']
    template_name = 'kits/create_or_update.html'
    success_url = reverse_lazy('kits:list')


class KitDelete(generic.DeleteView):
    """Class for deleting Kit objects"""
    model = Kit
    success_url = reverse_lazy('kits:list')