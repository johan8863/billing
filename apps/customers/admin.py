"""customers admin"""

# django
from django.contrib import admin

# local
from .models import Customer

admin.site.register(Customer)
