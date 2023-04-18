"""orders urls"""

# django
from django.urls import path

# local
from . import views

app_name = 'orders'
urlpatterns = [
    path('list/', views.OrderList.as_view(), name='list'),
    path('add/', views.OrderCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.OrderUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.OrderDelete.as_view(), name='delete'),
]