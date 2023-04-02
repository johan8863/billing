"""items apps config module"""

from django.apps import AppConfig


class ItemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # the name attribute must be the full python path
    # see https://docs.djangoproject.com/en/4.1/ref/applications/#configurable-attributes
    name = 'apps.item'
