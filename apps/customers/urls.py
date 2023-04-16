"""customers urls"""

# django
from django.urls import path

# local
from . import views

app_name = 'customers'
urlpatterns = [
    path('list/', views.CustomerList.as_view(), name='list'),
    path('add/', views.CustomerCreate.as_view(), name='create'),
]