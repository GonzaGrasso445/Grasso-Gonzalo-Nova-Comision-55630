from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#---------------------------Modelo Producto -----------------------------------------------------
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
#---------------------------Modelo Empleados -----------------------------------------------------
class Empleados (models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    cargo = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"


#---------------------------Modelo Sucursales -----------------------------------------------------
class Sucursales (models.Model):
    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"

#---------------------------Modelo Ofertas -----------------------------------------------------
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


#---------------------------Modelo Proveedores -----------------------------------------------------
class Proveedores (models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    empresa = models.CharField(max_length=60)
    rubro = models.CharField(max_length=60)
    cuit = models.IntegerField()
    direccion = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.empresa}"

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

#---------------------------Modelo RRHH -----------------------------------------------------
class Rrhh (models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    profesion = models.CharField(max_length=60)
    edad = models.IntegerField()
    email = models.EmailField()
    direccion = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.nombre,self.apellido}"

    class Meta:
        verbose_name = "Rrhh"
        verbose_name_plural = "Rrhh"



#---------------------------Modelo Avatar -----------------------------------------------------

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user,self.imagen}"