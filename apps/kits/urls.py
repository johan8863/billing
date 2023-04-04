"""kits urls"""

# django
from django.urls import path

# local
from . import views

app_name = 'kits'
urlpatterns = [
    path('list/', views.KitList.as_view(), name='list_kits'),
]