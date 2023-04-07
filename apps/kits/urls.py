"""kits urls"""

# django
from django.urls import path

# local
from . import views

app_name = 'kits'
urlpatterns = [
    path('list/', views.KitList.as_view(), name='list'),
    path('add/', views.KitCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.KitUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.KitDelete.as_view(), name='delete'),
]