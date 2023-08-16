from django.db import models

# Create your models here.

class Productos (models.Model):
    nombre = models.CharField(max_length=60)
    marca = models.CharField(max_length=60)
    tipo_Empaque = models.CharField(max_length=60)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering =['nombre']

class Empleados (models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    cargo = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"



class Sucursales (models.Model):
    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"


class Ofertas (models.Model):
    nombre = models.CharField(max_length=60)
    marca = models.CharField(max_length=60)
    tipo_Empaque = models.CharField(max_length=60)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name = "Oferta"
        verbose_name_plural = "Ofertas"