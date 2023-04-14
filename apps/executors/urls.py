"""executos urls"""

# django
from django.urls import path

# local
from . import views

app_name = 'executors'
urlpatterns = [
    path('list/', views.ExecutorList.as_view(), name='list'),
]