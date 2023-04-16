"""executos urls"""

# django
from django.urls import path

# local
from . import views

app_name = 'executors'
urlpatterns = [
    path('list/', views.ExecutorList.as_view(), name='list'),
    path('add/', views.ExecutorCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.ExecutorUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.ExecutorDelete.as_view(), name='delete'),
]