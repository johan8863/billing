"""items urls"""

# django
from django.urls import path

# local
from . import views

app_name = 'items'
urlpatterns = [
    path('list/', views.ItemList.as_view(), name='list'),
    path('add/', views.ItemCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.ItemUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.ItemDelete.as_view(), name='delete'),
]