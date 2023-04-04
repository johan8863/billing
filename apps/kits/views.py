"""kits views"""

# django
from django.views import generic

# local
from .models import Kit


class KitList(generic.ListView):
    """class to list kits objects"""
    queryset = Kit.objects.all()
    context_object_name = 'kits'
    template_name = 'kits/list.html'