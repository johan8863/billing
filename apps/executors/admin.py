"""executor admin"""

# django
from django.contrib import admin

# local
from .models import Executor

admin.site.register(Executor)
