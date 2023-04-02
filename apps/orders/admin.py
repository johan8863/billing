"""orders admin"""

# django
from django.contrib import admin

# local
from .models import Order

admin.site.register(Order)
