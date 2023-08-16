from django import forms

class ProductosForms(forms.Form):
    nombre = forms.CharField(max_length=60, required=True)
    marca = forms.CharField(max_length=60, required=True)
    tipo_Empaque = forms.CharField(max_length=60, required=True)
    precio = forms.IntegerField(required=True)



class EmpleadosForms(forms.Form):
    nombre = forms.CharField(max_length=60, required=True)
    apellido = forms.CharField(max_length=60, required=True)
    cargo = forms.CharField(max_length=60, required=True)
 



class SucursalesForms(forms.Form):
    nombre = forms.CharField(max_length=60, required=True)
    direccion = forms.CharField(max_length=60, required=True)
    tipo_Empaque = forms.EmailField(required=True)
  


class OfertasForms(forms.Form):
    nombre = forms.CharField(max_length=60, required=True)
    marca = forms.CharField(max_length=60, required=True)
    tipo_Empaque = forms.CharField(max_length=60, required=True)
    precio = forms.IntegerField(required=True)
    