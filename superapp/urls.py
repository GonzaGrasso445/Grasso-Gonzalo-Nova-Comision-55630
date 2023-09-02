from django.urls import path,include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [


    path('',suc , name ="suc"),
#-----------------------------------url Productos----------------------------
   path('productos/',productos , name ="productos"),
   path('productoform_adicional/',productoForm_adicional , name ="productoform_adicional"),
   path('buscarproducto/',buscarProducto , name ="buscarproducto"),
   path('buscar/',buscar , name ="buscar"),
   path('update_producto/<id_p>/',updateProductos , name ="update_producto"),
   path('delete_producto/<id_p>/',deleteProductos , name ="delete_producto"),
   path('create_producto/',createProductos , name ="create_producto"),

#-----------------------------------url Empleados----------------------------
   path('empleados/',empleados , name ="empleados"),
   path('empleadoform_adicional/',empleadoForm_adicional , name ="empleadoform_adicional"),
   path('buscarempleado/',buscarEmpleado , name ="buscarempleado"),
   path('buscar1/',buscar1 , name ="buscar1"),
   path('update_empleado/<id_e>/',updateEmpleados, name ="update_empleado"),
   path('delete_empleado/<id_e>/',deleteEmpleados , name ="delete_empleado"),
   path('create_empleado/',createEmpleados , name ="create_empleado"),

#-----------------------------------url Sucursales----------------------------
    path('sucursales/',sucursales , name ="sucursales"),
    path('sucursalform_adicional/',sucursalForm_adicional , name ="sucursalform_adicional"),
    path('buscarsucursal/',buscarSucursal , name ="buscarsucursal"),
    path('buscar3/',buscar3 , name ="buscar3"),
    path('update_sucursal/<id_s>/',updateSucursales, name ="update_sucursal"),
    path('delete_sucursal/<id_s>/',deleteSucursales , name ="delete_sucursal"),
    path('create_sucursal/',createSucursales , name ="create_sucursal"),

#-----------------------------------url Ofertas----------------------------
    path('ofertas/',ofertas , name ="ofertas"),
    path('oferta_form_adicional/',ofertaForm_adicional , name ="oferta_form_adicional"),
    path('buscaroferta/',buscarOferta , name ="buscaroferta"),
    path('buscar4/',buscar4 , name ="buscar4"),
    path('update_oferta/<id_o>/',updateOfertas, name ="update_oferta"),
    path('delete_oferta/<id_o>/',deleteOfertas , name ="delete_oferta"),
    path('create_oferta/',createOfertas , name ="create_oferta"),


#-----------------------------------url Proveedores----------------------------
    path('proveedores/',proveedores , name ="proveedores"),
    path('proveedores_form_adicional/',proveedoresForm_adicional , name ="proveedores_form_adicional"),
    path('buscarproveedores/',buscarProveedores , name ="buscarproveedores"),
    path('buscar5/',buscar5 , name ="buscar5"),
    path('update_proveedor/<id_a>/',updateProveedores, name ="update_proveedor"),
    path('delete_proveedor/<id_a>/',deleteProveedores , name ="delete_proveedor"),
    path('create_proveedor/',createProveedores , name ="create_proveedor"),

#-----------------------------------url Rrhh----------------------------
    path('rrhh/',rrhh , name ="rrhh"),
    path('rrhh_form_adicional/',rrhhForm_adicional , name ="rrhh_form_adicional"),
    path('buscarrrhh/',buscarRrhh , name ="buscarrrhh"),
    path('buscar6/',buscar6 , name ="buscar6"),
    path('update_rrhh/<id_b>/',updateRrhh, name ="update_rrhh"),
    path('delete_rrhh/<id_b>/',deleteRrhh , name ="delete_rrhh"),
    path('create_rrhh/',createRrhh , name ="create_rrhh"),


#-----------------------------------url Login/ Logout----------------------------

    path('login/',login_request , name ="login"),
    path('logout/',LogoutView.as_view(template_name="superapp/logout.html") , name ="logout"),
    path('registro/',register , name ="registro"),



#----------------------------------- url Editar Perfiles----------------------------
    path('editar_perfil/',editarPerfil , name ="editar_perfil"),


#----------------------------------- url Agregar Avatar----------------------------

    path('agregar_avatar/',agregarAvatar , name ="agregar_avatar"),

#-----------------------------------url Sobre Gonza Grasso----------------------------
    path('sobremi/',sobreMi , name ="sobreMi"),


]




