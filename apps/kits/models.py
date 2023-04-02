"""kits models"""

# django
from django.db import models

class Kit(models.Model):
    """Kit model, it'll be used to select the kind of kit in the order"""
    name = models.CharField('Nombre', max_length=50)
    # attribute to deal with deactivation instead of deletion 
    # when an objetc has relationships
    is_active = models.BooleanField(default=True, editable=False)

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
    
    def __str__(self):
        """Returns  the string object representation"""
        return self.name