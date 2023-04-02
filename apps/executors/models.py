"""executors models"""

# django
from django.db import models

class Executor(models.Model):
    """The person who performs the job in an order"""
    full_name = models.CharField('Nombre', max_length=150)
    license_number = models.CharField('Licencia', max_length=10)
    personal_id = models.CharField('No. CI', max_length=11)

    class Meta:
        ordering = ['full_name']
        verbose_name = 'Ejecutor'
        verbose_name_plural = 'Ejecutores'
    
    def __str__(self):
        """Returns  the string object representation"""
        return self.full_name