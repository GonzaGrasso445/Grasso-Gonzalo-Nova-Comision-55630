from django.urls import path,include
from .views import *

urlpatterns = [

    path('',suc , name ="suc"),
    path('productos/',productos , name ="productos"),
    path('empleados/',empleados , name ="empleados"),
    path('sucursales/',sucursales , name ="sucursales"),
    path('ofertas/',ofertas , name ="ofertas"),



    path('producto_form/',productoForm , name ="producto_form"),
    path('empleado_form/',empleadoForm , name ="empleado_form"),
    path('sucursal_form/',sucursalForm , name ="sucursal_form"),
    path('oferta_form/',ofertaForm , name ="oferta_form"),

    path('productoform_adicional/',productoForm_adicional , name ="productoform_adicional"),
    path('empleadoform_adicional/',empleadoForm_adicional , name ="empleadoform_adicional"),
    path('sucursalform_adicional/',sucursalForm_adicional , name ="sucursalform_adicional"),
    path('oferta_form_adicional/',ofertaForm_adicional , name ="oferta_form_adicional"),


   path('buscarproducto/',buscarProducto , name ="buscarproducto"),
   path('buscar/',buscar , name ="buscar"),

   path('buscarempleado/',buscarEmpleado , name ="buscarempleado"),
   path('buscar1/',buscar1 , name ="buscar1"),

   path('buscarsucursal/',buscarSucursal , name ="buscarsucursal"),
   path('buscar3/',buscar3 , name ="buscar3"),

    path('buscaroferta/',buscarOferta , name ="buscaroferta"),
   path('buscar4/',buscar4 , name ="buscar4"),

]