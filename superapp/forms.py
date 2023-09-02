from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#---------------------------Formulario Productos -----------------------------------------------------
class ProductosForms(forms.Form):
    nombre = forms.CharField(label="Nombre",max_length=60, required=True)
    marca = forms.CharField(label="Marca",max_length=60, required=True)
    tipo_Empaque = forms.CharField(label="Tipo de Empaque",max_length=60, required=True)
    precio = forms.IntegerField(label="Precio",required=True)

#---------------------------Formulario Empleados -----------------------------------------------------

class EmpleadosForms(forms.Form):
    nombre = forms.CharField(label="Nombre",max_length=60, required=True)
    apellido = forms.CharField(label="Apellido",max_length=60, required=True)
    cargo = forms.CharField(label="Cargo",max_length=60, required=True)
 

#---------------------------Formulario Sucursales -----------------------------------------------------

class SucursalesForms(forms.Form):
    nombre = forms.CharField(label="Nombre",max_length=60, required=True)
    direccion = forms.CharField(label="Direccion",max_length=60, required=True)
    email = forms.EmailField(label="Email",required=True)
  
#---------------------------Formulario Ofertas -----------------------------------------------------

class OfertasForms(forms.Form):
    nombre = forms.CharField(label="Nombre",max_length=60, required=True)
    marca = forms.CharField(label="Marca",max_length=60, required=True)
    tipo_Empaque = forms.CharField(label="Tipo de Empaque",max_length=60, required=True)
    precio = forms.IntegerField(label="Precio",required=True)

#---------------------------Formulario Proveedores -----------------------------------------------------

class ProveedoresForms(forms.Form):
    nombre = forms.CharField(label="Nombre",max_length=60, required=True)
    apellido = forms.CharField(label="Apellido",max_length=60, required=True)
    empresa  = forms.CharField(label="Empresa",max_length=60, required=True)
    rubro  = forms.CharField(label="Rubro",max_length=60, required=True)
    cuit = forms.IntegerField(label="Cuit",required=True)
    direccion  = forms.CharField(label="Direccion",max_length=60, required=True)

#---------------------------Formulario Rrhh -----------------------------------------------------
class RrhhForms(forms.Form):
    nombre = forms.CharField(label="Nombre",max_length=60, required=True)
    apellido = forms.CharField(label="Apellido",max_length=60, required=True)
    profesion = forms.CharField(label="Profesion",max_length=60, required=True)
    edad = forms.IntegerField(label="Edad",required=True)
    email = forms.EmailField(label="Email",max_length=60, required=True)
    direccion = forms.CharField(label="Direccion",max_length=60, required=True)


#---------------------------Formulario de Registro de Usuarios  -----------------------------------------------------

class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label = "Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label = "Confirmar Contraseña", widget= forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username','email','password1','password2']

#---------------------------Formulario de Edicion de Usuarios  -----------------------------------------------------

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label = "Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label = "Confirmar Contraseña", widget= forms.PasswordInput)
    first_name = forms.CharField(label = "Nombre Completo", max_length=50,required=False)
    last_name = forms.CharField(label = "Apellido", max_length=50,required=False)
    
    class Meta:
      model = User
      fields = ['email','password1','password2','first_name','last_name']


#---------------------------Formulario Avatar Formulario -----------------------------------------------------
class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)