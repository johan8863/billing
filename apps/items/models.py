"""items models"""

# django
from django.db import models

class Item(models.Model):
    """
    The source model of the software. It represents the 'items'
    registered in service orders and bills. They can be six types as shown 
    in the item_type attribute.
    """
    ITEM_TYPES = [
        ('product', 'Producto'),
        ('concept', 'Concepto'),
        ('repair', 'Reparación'),
        ('maintenace', 'Mtto'),
        ('install', 'Instal/Mont'),
        ('unmounting', 'Desmontaje'),
    ]

    code = models.CharField('Código', max_length=15)
    name = models.CharField('Nombre', max_length=120)
    item_type = models.CharField(max_length=11, choices=ITEM_TYPES)
    price = models.FloatField('Precio')
    # attribute to deal with deactivation instead of deletion 
    # when an objetc has relationships
    is_active = models.BooleanField(default=True, editable=False)

    class Meta:
        ordering = ['name']
        verbose_name = 'Elemento'
        verbose_name_plural = 'Elementos'
    
    def __str__(self):
        """Returns  the string object representation"""
        return self.name