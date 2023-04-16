"""customers urls"""

# django
from django.urls import path

# local
from . import views

app_name = 'customers'
urlpatterns = [
    path('list/', views.CustomerList.as_view(), name='list'),
    path('add/', views.CustomerCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.CustomerUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.CustomerDelete.as_view(), name='delete'),
]