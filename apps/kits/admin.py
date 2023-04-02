"""kits admin"""

# django
from django.contrib import admin

# local
from .models import Kit

admin.site.register(Kit)
