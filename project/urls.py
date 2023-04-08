"""project urls"""

from django.contrib import admin
from django.urls import include, path
from django.views import generic

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', generic.TemplateView.as_view(template_name='home.html')),
    path('kits/', include('apps.kits.urls')),
    path('items/', include('apps.items.urls')),
]
