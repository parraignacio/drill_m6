from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class VehiculoModel(models.Model):
    marca_opts = [
        ("1", 'Ford'),
        ("2", 'Fiat'),
        ("3", 'Chevrolet'),
        ("4", 'Toyota'),
    ]

    categoria_opts = [
        ('P', 'Particular'),
        ('T', 'Transporte'),
        ('C', 'Carga'),
    ]

    marca = models.CharField(max_length=20, choices=marca_opts, default= 'Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=categoria_opts, default= 'Particular')
    precio = models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Vehiculos"
        ordering = ["-fecha_creacion"]
    
    def get_condicion(self):
        if self.precio <= 10000:
            return "Bajo"
        elif 10000 < self.precio <= 30000:
            return "Medio"
        else:
            return "Alto"
        
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Serial Carrocería: {self.serial_carroceria}, Serial Motor: {self.serial_motor}, Categoría: {self.categoria}, Precio: {self.precio}, Fecha de Creación: {self.fecha_creacion}, Fecha de Modificación: {self.fecha_modificacion}"

# Permiso para visualizar
""" visualizar_permission = Permission.objects.create(
codename='visualizar_catalogo',
name='Permiso para ver',
content_type=ContentType.objects.get_for_model(VehiculoModel),
) """