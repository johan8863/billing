"""kits views"""

# django
from django.views import generic

# local
from .models import Kit


class KitList(generic.ListView):
    """class to list kits objects"""
    model = Kit
    paginate_by = 8
    template_name = 'kits/list.html'