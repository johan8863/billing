"""orders admin"""

# django
from django.contrib import admin

# local
from .models import Order, ItemTimes

admin.site.register(Order)
admin.site.register(ItemTimes)
