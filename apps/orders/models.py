"""orders models"""

# django
from django.db import models

# local
from ..customers.models import Customer
from ..kits.models import Kit
from ..items.models import Item
from ..executors.models import Executor


class Order(models.Model):
    """Pre Bill document to register job details performed"""
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, verbose_name="Cliente")
    symptom = models.CharField('Síntoma', max_length=100)
    flaw = models.CharField('Defecto', max_length=100)
    repair_description = models.CharField('Reparación', max_length=100)
    folio = models.CharField('No. folio', max_length=10)
    # next four attributes are related to the modality of the order
    check_diagnosis = models.BooleanField('Revisión/Diagnóstico')
    repair = models.BooleanField('Reparacón')
    install = models.BooleanField('Instal./Mont./Desmont.')
    maintenance = models.BooleanField('Mtto')
    # end of modality set
    kit = models.ForeignKey(Kit, on_delete=models.SET_NULL, null=True, verbose_name="Equipo")
    kit_brand = models.CharField('Marca', max_length=20)
    kit_model = models.CharField('Modelo', max_length=20)
    kit_serial = models.CharField('No. de serie o Inv.', max_length=20)
    job_description = models.TextField('Descripción del trabajo realizado', blank=True, null=True)
    items = models.ManyToManyField(Item, verbose_name='Artículo o Servicio')
    executor = models.ForeignKey(
        Executor,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Ejecutor'
    )
    # customer_charge = models.CharField('Cargo', max_length=25)
    # customer_name = models.CharField('Nombre', max_length=25)
    # customer_personal_id = models.CharField('No. CI', max_length=11)
    executor_signature_date = models.DateField('Fecha')
    customer_signature_date = models.DateField('Fecha')
    # attribute to deal with deactivation instead of deletion 
    # when an objetc has relationships
    is_active = models.BooleanField(default=True, editable=False)

    class Meta:
        ordering = ['executor_signature_date']
        verbose_name = 'Orden de Servicio'
        verbose_name_plural = 'Órdenes de Servicio'
    
    def __str__(self):
        """Returns  the string object representation"""
        return self.customer.name