
#---------------------------Import -----------------------------------------------------

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth       import authenticate,login
from django.contrib.auth.decorators       import login_required
from django.contrib.auth.models import User




from .models import Productos,Empleados,Ofertas,Sucursales,Proveedores,Rrhh,Avatar
from.forms import ProductosForms, EmpleadosForms,SucursalesForms,OfertasForms,ProveedoresForms,RrhhForms,RegistroUsuariosForm,UserEditForm,AvatarFormulario

# Create your views here.

#--------------------------- -----------------------------------------------------
def sobreMi (request):
    return render (request, "superapp/sobreMi.html")


def suc (request):
    return render (request, "superapp/suc.html")
@login_required
def productos (request):
    contexto = {'productos': Productos.objects.all(),'producto1': 'Listado de Productos'}
    return render (request, "superapp/productos.html", contexto)

@login_required
def empleados (request):
    contexto1 = {'empleados': Empleados.objects.all(),'empleados1': 'Listado de Empleados'}
    return render (request, "superapp/empleados.html",contexto1)

@login_required
def sucursales (request):
    contexto3 = {'sucursales': Sucursales.objects.all(),'sucursales1': 'Listado de Sucursales'}
    return render (request, "superapp/sucursales.html",contexto3)

@login_required
def ofertas (request):
    contexto4 = {'ofertas': Ofertas.objects.all()}
    return render (request, "superapp/ofertas.html",contexto4)

@login_required
def proveedores (request):
    contexto5 = {'proveedores': Proveedores.objects.all()}
    return render (request, "superapp/proveedores.html",contexto5)
@login_required
def rrhh (request):
    contexto6 = {'rrhh': Rrhh.objects.all()}
    return render (request, "superapp/rrhh.html",contexto6)




#---------------------------Formularios y Busqueda Productos -----------------------------------------------------
@login_required
def productoForm_adicional(request):
    if request.method == "POST":
       miFormulario = ProductosForms(request.POST)
       if miFormulario.is_valid():
           producto_nombre = miFormulario.cleaned_data.get ('nombre')
           producto_marca = miFormulario.cleaned_data.get ('marca')
           producto_tipo_Empaque = miFormulario.cleaned_data.get ('tipo_Empaque')
           producto_precio= miFormulario.cleaned_data.get ('precio')
           producto = Productos(nombre = producto_nombre, marca = producto_marca,tipo_Empaque =producto_tipo_Empaque,precio = producto_precio)
           producto.save()
           return render (request, "superapp/base.html")


    else:
        miFormulario = ProductosForms()

    return render(request, "superapp/productoForm_adicional.html",{"form":miFormulario})

@login_required
def buscarProducto(request):
    return render(request, "superapp/buscarProducto.html")

@login_required
def buscar(request):
    if request.GET['buscar']:
        busqueda_avanzada = request.GET['buscar']
        productos =Productos.objects.filter(nombre__icontains=busqueda_avanzada)
        contexto ={"productos": productos}
        return render(request, "superapp/productos.html", contexto)
    
    return HttpResponse("No se ingresaron datos")



#---------------------------Formularios y Busqueda Empleados -----------------------------------------------------

@login_required
def empleadoForm_adicional(request):
    if request.method == "POST":
       miFormulario1 = EmpleadosForms(request.POST)
       if miFormulario1.is_valid():
           empleado_nombre = miFormulario1.cleaned_data.get ('nombre')
           empleado_apellido = miFormulario1.cleaned_data.get ('apellido')
           empleado_cargo = miFormulario1.cleaned_data.get ('cargo')
           empleado = Empleados(nombre = empleado_nombre, apellido = empleado_apellido,cargo =empleado_cargo)
           empleado.save()
           return render (request, "superapp/base.html")


    else:
        miFormulario1 = EmpleadosForms()

    return render(request, "superapp/empleadoForm_adicional.html",{"form":miFormulario1})


@login_required
def buscarEmpleado(request):
    return render(request, "superapp/buscarEmpleado.html")

@login_required
def buscar1(request):
    if request.GET['buscar1']:
        busqueda_avanzada1 = request.GET['buscar1']
        empleados =Empleados.objects.filter(nombre__icontains=busqueda_avanzada1)
        contexto1 ={"empleados": empleados}
        return render (request, "superapp/empleados.html",contexto1)

    
    return HttpResponse("No se ingresaron datos")



#---------------------------Formularios y Busqueda Sucursales -----------------------------------------------------
@login_required
def sucursalForm_adicional(request):
    if request.method == "POST":
       miFormulario2 = SucursalesForms(request.POST)
       if miFormulario2.is_valid():
           sucursal_nombre = miFormulario2.cleaned_data.get ('nombre')
           sucursal_direccion = miFormulario2.cleaned_data.get ('direccion')
           sucursal_email = miFormulario2.cleaned_data.get ('email')
           sucursal = Sucursales(nombre = sucursal_nombre, direccion = sucursal_direccion,email =sucursal_email)
           sucursal.save()
           return render (request, "superapp/base.html")


    else:
        miFormulario2 = SucursalesForms()

    return render(request, "superapp/sucursalForm_adicional.html",{"form":miFormulario2})

@login_required
def buscarSucursal(request):
    return render(request, "superapp/buscarSucursal.html")

@login_required
def buscar3(request):
    if request.GET['buscar3']:
        busqueda_avanzada2 = request.GET['buscar3']
        sucursales =Sucursales.objects.filter(nombre__icontains=busqueda_avanzada2)
        contexto3 ={"sucursales": sucursales}
        return render (request, "superapp/sucursales.html",contexto3)
    
    return HttpResponse("No se ingresaron datos")

#---------------------------Formularios y Busqueda Ofertas -----------------------------------------------------
@login_required
def ofertaForm_adicional(request):
    if request.method == "POST":
       miFormulario3 = OfertasForms(request.POST)
       if miFormulario3.is_valid():
           oferta_nombre = miFormulario3.cleaned_data.get ('nombre')
           oferta_marca = miFormulario3.cleaned_data.get ('marca')
           oferta_tipo_Empaque = miFormulario3.cleaned_data.get ('tipo_Empaque')
           oferta_precio= miFormulario3.cleaned_data.get ('precio')
           oferta = Ofertas(nombre = oferta_nombre, marca = oferta_marca,tipo_Empaque =oferta_tipo_Empaque,precio = oferta_precio)
           oferta.save()
           return render (request, "superapp/base.html")


    else:
        miFormulario3 = OfertasForms()

    return render(request, "superapp/ofertaForm_adicional.html",{"form":miFormulario3})


@login_required
def buscarOferta(request):
    return render(request, "superapp/buscarOferta.html")

@login_required
def buscar4(request):
    if request.GET['buscar4']:
        busqueda_avanzada4 = request.GET['buscar4']
        ofertas =Ofertas.objects.filter(nombre__icontains=busqueda_avanzada4)
        contexto4 ={"ofertas": ofertas}
        return render (request, "superapp/ofertas.html",contexto4)
    
    return HttpResponse("No se ingresaron datos")




#---------------------------Formularios y Busqueda Proveedores -----------------------------------------------------
@login_required
def proveedoresForm_adicional(request):
    if request.method == "POST":
       miFormulario4 = ProveedoresForms(request.POST)
       if miFormulario4.is_valid():
           proveedores_nombre = miFormulario4.cleaned_data.get ('nombre')
           proveedores_apellido = miFormulario4.cleaned_data.get ('apellido')
           proveedores_empresa = miFormulario4.cleaned_data.get ('empresa')
           proveedores_rubro= miFormulario4.cleaned_data.get ('rubro')
           proveedores_cuit= miFormulario4.cleaned_data.get ('cuit')
           proveedores_direccion= miFormulario4.cleaned_data.get ('direccion')


           proveedores = Proveedores(nombre = proveedores_nombre, apellido = proveedores_apellido,
                                     empresa =proveedores_empresa,rubro = proveedores_rubro,cuit=proveedores_cuit,direccion=proveedores_direccion)
           proveedores.save()
           return render (request, "superapp/base.html")


    else:
        miFormulario4 = ProveedoresForms()

    return render(request, "superapp/proveedoresForm_adicional.html",{"form":miFormulario4})


@login_required
def buscarProveedores(request):
    return render(request, "superapp/buscarProveedores.html")

@login_required
def buscar5(request):
    if request.GET['buscar5']:
        busqueda_avanzada5 = request.GET['buscar5']
        proveedores =Proveedores.objects.filter(nombre__icontains=busqueda_avanzada5)
        contexto5 ={"proveedores": proveedores}
        return render (request, "superapp/proveedores.html",contexto5)
    
    return HttpResponse("No se ingresaron datos")


#---------------------------Formularios y Busqueda Rrhh -----------------------------------------------------
@login_required
def rrhhForm_adicional(request):
    if request.method == "POST":
       miFormulario5 = RrhhForms(request.POST)
       if miFormulario5.is_valid():
           rrhh_nombre = miFormulario5.cleaned_data.get ('nombre')
           rrhh_apellido = miFormulario5.cleaned_data.get ('apellido')
           rrhh_profesion = miFormulario5.cleaned_data.get ('profesion')
           rrhh_edad= miFormulario5.cleaned_data.get ('edad')
           rrhh_email= miFormulario5.cleaned_data.get ('email')
           rrhh_direccion= miFormulario5.cleaned_data.get ('direccion')


           rrhh = Rrhh(nombre = rrhh_nombre, apellido = rrhh_apellido,
                                     profesion =rrhh_profesion,edad = rrhh_edad,email=rrhh_email,direccion=rrhh_direccion)
           rrhh.save()
           return render (request, "superapp/base.html")


    else:
        miFormulario5 = RrhhForms()

    return render(request, "superapp/rrhhForm_adicional.html",{"form":miFormulario5})


@login_required
def buscarRrhh(request):
    return render(request, "superapp/buscarRrhh.html")

@login_required
def buscar6(request):
    if request.GET['buscar6']:
        busqueda_avanzada6 = request.GET['buscar6']
        rrhh =Rrhh.objects.filter(nombre__icontains=busqueda_avanzada6)
        contexto6 ={"rrhh": rrhh}
        return render (request, "superapp/rrhh.html",contexto6)
    
    return HttpResponse("No se ingresaron datos")



#---------------------------Edicion y Delete and Create Productos -----------------------------------------------------
@login_required
def updateProductos(request,id_p):
    producto = Productos.objects.get(id=id_p)
    if request.method == "POST":
        miForm = ProductosForms(request.POST)
        if miForm.is_valid():
            producto.nombre = miForm.cleaned_data.get('nombre')
            producto.marca = miForm.cleaned_data.get('marca')
            producto.tipo_Empaque = miForm.cleaned_data.get('tipo_Empaque')
            producto.precio = miForm.cleaned_data.get('precio')
            producto.save()
            return redirect(reverse_lazy('productos'))
    else:
        miForm = ProductosForms(initial={
            'nombre':producto.nombre,
            'marca': producto.marca,
            'tipo_Empaque': producto.tipo_Empaque,
            'precio': producto.precio,
        })
    return render(request,"superapp/productoForm_adicional.html",{'form': miForm})

@login_required
def deleteProductos(request,id_p):
    producto = Productos.objects.get(id=id_p)
    producto.delete()
    return redirect(reverse_lazy('productos'))

@login_required
def createProductos(request):
    if request.method == "POST":
        miForm = ProductosForms(request.POST)
        if miForm.is_valid():
            p_nombre = miForm.cleaned_data.get('nombre')
            p_marca = miForm.cleaned_data.get('marca')
            p_tipo_Empaque = miForm.cleaned_data.get('tipo_Empaque')
            p_precio = miForm.cleaned_data.get('precio')
            producto = Productos (nombre =p_nombre,marca=p_marca,tipo_Empaque=p_tipo_Empaque,precio=p_precio)
            producto.save()
            return redirect(reverse_lazy('productos'))
    else:
        miForm = ProductosForms()
    return render(request,"superapp/productoForm_adicional.html",{'form': miForm})



#---------------------------Edicion y Delete and Create Empleados -----------------------------------------------------
@login_required
def updateEmpleados(request,id_e):
    empleado = Empleados.objects.get(id=id_e)
    if request.method == "POST":
        miForm1 = EmpleadosForms(request.POST)
        if miForm1.is_valid():
            empleado.nombre = miForm1.cleaned_data.get('nombre')
            empleado.apellido = miForm1.cleaned_data.get('apellido')
            empleado.cargo = miForm1.cleaned_data.get('cargo')
            empleado.save()
            return redirect(reverse_lazy('empleados'))
    else:
        miForm1 = EmpleadosForms(initial={
            'nombre':empleado.nombre,
            'apellido': empleado.apellido,
            'cargo': empleado.cargo,
        })
    return render(request,"superapp/empleadoForm_adicional.html",{'form': miForm1})

@login_required
def deleteEmpleados(request,id_e):
    empleado = Empleados.objects.get(id=id_e)
    empleado.delete()
    return redirect(reverse_lazy('empleados'))

@login_required
def createEmpleados(request):
    if request.method == "POST":
        miForm1 = EmpleadosForms(request.POST)
        if miForm1.is_valid():
            p_nombre = miForm1.cleaned_data.get('nombre')
            p_apellido = miForm1.cleaned_data.get('apellido')
            p_cargo = miForm1.cleaned_data.get('cargo')
            empleado = Empleados (nombre =p_nombre,apellido=p_apellido,cargo=p_cargo)
            empleado.save()
            return redirect(reverse_lazy('empleados'))
    else:
        miForm1 = EmpleadosForms()
    return render(request,"superapp/empleadoForm_adicional.html",{'form': miForm1})




#---------------------------Edicion y Delete and Create Sucursales -----------------------------------------------------
@login_required
def updateSucursales(request,id_s):
    sucursal = Sucursales.objects.get(id=id_s)
    if request.method == "POST":
        miForm2 = SucursalesForms(request.POST)
        if miForm2.is_valid():
            sucursal.nombre = miForm2.cleaned_data.get('nombre')
            sucursal.direccion = miForm2.cleaned_data.get('direccion')
            sucursal.email = miForm2.cleaned_data.get('email')
            sucursal.save()
            return redirect(reverse_lazy('sucursales'))
    else:
        miForm2= SucursalesForms(initial={
            'nombre':sucursal.nombre,
            'direccion': sucursal.direccion,
            'email': sucursal.email,
        })
    return render(request,"superapp/sucursalForm_adicional.html",{'form': miForm2})

@login_required
def deleteSucursales(request,id_s):
    sucursal = Sucursales.objects.get(id=id_s)
    sucursal.delete()
    return redirect(reverse_lazy('sucursales'))


@login_required
def createSucursales(request):
    if request.method == "POST":
        miForm2 = SucursalesForms(request.POST)
        if miForm2.is_valid():
            s_nombre = miForm2.cleaned_data.get('nombre')
            s_direccion = miForm2.cleaned_data.get('direccion')
            s_email = miForm2.cleaned_data.get('email')
            sucursal = Sucursales (nombre =s_nombre,direccion=s_direccion,email=s_email)
            sucursal.save()
            return redirect(reverse_lazy('sucursales'))
    else:
        miForm2 = SucursalesForms()
    return render(request,"superapp/sucursalForm_adicional.html",{'form': miForm2})



#---------------------------Edicion y Delete and Create Ofertas -----------------------------------------------------
@login_required
def updateOfertas(request,id_o):
    oferta = Ofertas.objects.get(id=id_o)
    if request.method == "POST":
        miForm3 = OfertasForms(request.POST)
        if miForm3.is_valid():
            oferta.nombre = miForm3.cleaned_data.get('nombre')
            oferta.marca = miForm3.cleaned_data.get('marca')
            oferta.tipo_Empaque = miForm3.cleaned_data.get('tipo_Empaque')
            oferta.precio = miForm3.cleaned_data.get('precio')            
            oferta.save()
            return redirect(reverse_lazy('ofertas'))
    else:
        miForm3= OfertasForms(initial={
            'nombre':oferta.nombre,
            'marca': oferta.marca,
            'tipo_Empaque': oferta.tipo_Empaque,
            'precio': oferta.precio,
        })
    return render(request,"superapp/ofertaForm_adicional.html",{'form': miForm3})

@login_required
def deleteOfertas(request,id_o):
    oferta = Ofertas.objects.get(id=id_o)
    oferta.delete()
    return redirect(reverse_lazy('ofertas'))

@login_required
def createOfertas(request):
    if request.method == "POST":
        miForm3 = OfertasForms(request.POST)
        if miForm3.is_valid():
            o_nombre = miForm3.cleaned_data.get('nombre')
            o_marca = miForm3.cleaned_data.get('marca')
            o_tipo_Empaque= miForm3.cleaned_data.get('tipo_Empaque')
            o_precio = miForm3.cleaned_data.get('precio') 
            oferta = Ofertas (nombre =o_nombre,marca=o_marca,tipo_Empaque=o_tipo_Empaque,precio=o_precio)
            oferta.save()
            return redirect(reverse_lazy('ofertas'))
    else:
        miForm3 = OfertasForms()
    return render(request,"superapp/ofertaForm_adicional.html",{'form': miForm3})

#---------------------------Actualizacion Proveedores -----------------------------------------------------
@login_required
def updateProveedores(request,id_a):
    proveedor = Proveedores.objects.get(id=id_a)
    if request.method == "POST":
        miForm4 = ProveedoresForms(request.POST)
        if miForm4.is_valid():
            proveedor.nombre = miForm4.cleaned_data.get('nombre')
            proveedor.apellido = miForm4.cleaned_data.get('apellido')
            proveedor.empresa = miForm4.cleaned_data.get('empresa')
            proveedor.rubro = miForm4.cleaned_data.get('rubro')   
            proveedor.cuit = miForm4.cleaned_data.get('cuit') 
            proveedor.direccion = miForm4.cleaned_data.get('direccion')          
            proveedor.save()
            return redirect(reverse_lazy('proveedores'))
    else:
        miForm4= ProveedoresForms(initial={
            'nombre':proveedor.nombre,
            'apellido': proveedor.apellido,
            'empresa': proveedor.empresa,
            'rubro': proveedor.rubro,
            'cuit': proveedor.cuit,
            'direccion': proveedor.direccion,
        })
    return render(request,"superapp/proveedoresForm_adicional.html",{'form': miForm4})


@login_required
def deleteProveedores(request,id_a):
    proveedor = Proveedores.objects.get(id=id_a)
    proveedor.delete()
    return redirect(reverse_lazy('proveedores'))

@login_required
def createProveedores(request):
    if request.method == "POST":
        miForm4 = ProveedoresForms(request.POST)
        if miForm4.is_valid():
            a_nombre = miForm4.cleaned_data.get('nombre')
            a_apellido = miForm4.cleaned_data.get('apellido')
            a_empresa= miForm4.cleaned_data.get('empresa')
            a_rubro = miForm4.cleaned_data.get('rubro') 
            a_cuit = miForm4.cleaned_data.get('cuit') 
            a_direccion = miForm4.cleaned_data.get('direccion') 
            proveedor = Proveedores (nombre =a_nombre,apellido=a_apellido,empresa=a_empresa,rubro=a_rubro,cuit=a_cuit,direccion=a_direccion)
            proveedor.save()
            return redirect(reverse_lazy('proveedores'))
    else:
        miForm4 = ProveedoresForms()
    return render(request,"superapp/proveedoresForm_adicional.html",{'form': miForm4})


#---------------------------Actualizacion Rrhh -----------------------------------------------------
@login_required
def updateRrhh(request,id_b):
    rrhh = Rrhh.objects.get(id=id_b)
    if request.method == "POST":
        miForm5 = RrhhForms(request.POST)
        if miForm5.is_valid():
            rrhh.nombre = miForm5.cleaned_data.get('nombre')
            rrhh.apellido = miForm5.cleaned_data.get('apellido')
            rrhh.profesion = miForm5.cleaned_data.get('profesion')
            rrhh.edad = miForm5.cleaned_data.get('edad')   
            rrhh.email = miForm5.cleaned_data.get('email') 
            rrhh.direccion = miForm5.cleaned_data.get('direccion')          
            rrhh.save()
            return redirect(reverse_lazy('rrhh'))
    else:
        miForm5= RrhhForms(initial={
            'nombre':rrhh.nombre,
            'apellido': rrhh.apellido,
            'profesion': rrhh.profesion,
            'edad': rrhh.edad,
            'email': rrhh.email,
            'direccion': rrhh.direccion,
        })
    return render(request,"superapp/rrhhForm_adicional.html",{'form': miForm5})

@login_required
def deleteRrhh(request,id_b):
    rrhh = Rrhh.objects.get(id=id_b)
    rrhh.delete()
    return redirect(reverse_lazy('rrhh'))

@login_required
def createRrhh(request):
    if request.method == "POST":
        miForm5 = RrhhForms(request.POST)
        if miForm5.is_valid():
            b_nombre = miForm5.cleaned_data.get('nombre')
            b_apellido = miForm5.cleaned_data.get('apellido')
            b_profesion= miForm5.cleaned_data.get('profesion')
            b_edad = miForm5.cleaned_data.get('edad') 
            b_email = miForm5.cleaned_data.get('email') 
            b_direccion = miForm5.cleaned_data.get('direccion') 
            rrhh = Rrhh (nombre =b_nombre,apellido=b_apellido,profesion=b_profesion,edad=b_edad,email=b_email,direccion=b_direccion)
            rrhh.save()
            return redirect(reverse_lazy('rrhh'))
    else:
        miForm5 = RrhhForms()
    return render(request,"superapp/rrhhForm_adicional.html",{'form': miForm5})



#---------------------------Login / Logout / Register -----------------------------------------------------

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request,data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request,user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar ="/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar
                return render(request,"superapp/base.html",{'mensaje': f"Bienvenidos al central {usuario}"})
            
            else:
                return render(request,"superapp/login.html",{'form': miForm, 'mensaje': f"Los datos ingresados son incorrectos"})
            

        else:
            return render(request,"superapp/login.html",{'form': miForm, 'mensaje': f"Los datos ingresados son incorrectos"})

            
    miForm = AuthenticationForm()
    return  render(request,"superapp/login.html",{'form': miForm})


def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request,"superapp/base.html")
            
    else:
        miForm = RegistroUsuariosForm()
                
        

    return render(request,"superapp/registro.html",{'form': miForm})

            
#---------------------------Editar Perfiles -----------------------------------------------------
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request,"superapp/base.html")
        else:
            return render(request,"superapp/editarPerfil.html", {'form': form,'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request,"superapp/editarPerfil.html",{'form': form,'usuario': usuario.username}) 
            

#---------------------------Agregar Avatar -----------------------------------------------------
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST,request.FILES)
        if form.is_valid():
            usu =User.objects.get(username=request.user)
            avatarOld = Avatar.objects.filter(user=usu)
            if len(avatarOld)>0:
                for i in range(len(avatarOld)):
                  avatarOld[0].delete()
            avatar = Avatar(user=usu,imagen=form.cleaned_data['imagen'])
            avatar.save()
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar']= imagen
            return render(request,"superapp/base.html")

    else:
        form = AvatarFormulario()
    return render(request,"superapp/agregarAvatar.html",{'form': form})


