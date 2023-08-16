from django.shortcuts import render
from django.http import HttpResponse

from .models import Productos,Empleados,Ofertas,Sucursales
from.forms import ProductosForms, EmpleadosForms,SucursalesForms,OfertasForms
# Create your views here.


def suc (request):
    return render (request, "superapp/suc.html")

def productos (request):
    contexto = {'productos': Productos.objects.all(),'producto1': 'Listado de Productos'}
    return render (request, "superapp/productos.html", contexto)


def empleados (request):
    contexto1 = {'empleados': Empleados.objects.all(),'empleados1': 'Listado de Empleados'}
    return render (request, "superapp/empleados.html",contexto1)


def sucursales (request):
    contexto3 = {'sucursales': Sucursales.objects.all(),'sucursales1': 'Listado de Sucursales'}
    return render (request, "superapp/sucursales.html",contexto3)


def ofertas (request):
    contexto4 = {'ofertas': Ofertas.objects.all()}
    return render (request, "superapp/ofertas.html",contexto4)


def productoForm (request):
    if request.method == "POST":
        prod = Productos(nombre = request.POST['nombre'],marca=request.POST['marca'],tipo_Empaque=request.POST['tipo_Empaque']
                         ,precio=request.POST['precio'])

        prod.save()
        return HttpResponse ("Sus datos fueron grabados")
    return render(request,"superapp/productoForm.html")

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


def buscarProducto(request):
    return render(request, "superapp/buscarProducto.html")

def buscar(request):
    if request.GET['buscar']:
        busqueda_avanzada = request.GET['buscar']
        productos =Productos.objects.filter(nombre__icontains=busqueda_avanzada)
        contexto ={"productos": productos}
        return render(request, "superapp/productos.html", contexto)
    
    return HttpResponse("No se ingresaron datos")



def empleadoForm (request):
    if request.method == "POST":
        emple = Empleados(nombre = request.POST['nombre'],apellido=request.POST['apellido'],cargo=request.POST['cargo'])

        emple.save()
        return HttpResponse ("Sus datos fueron grabados")
    return render(request,"superapp/empleadoForm.html")


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



def buscarEmpleado(request):
    return render(request, "superapp/buscarEmpleado.html")

def buscar1(request):
    if request.GET['buscar1']:
        busqueda_avanzada1 = request.GET['buscar1']
        empleados =Empleados.objects.filter(nombre__icontains=busqueda_avanzada1)
        contexto1 ={"empleados": empleados}
        return render (request, "superapp/empleados.html",contexto1)

    
    return HttpResponse("No se ingresaron datos")

def sucursalForm (request):
    if request.method == "POST":
        sucur = Sucursales(nombre = request.POST['nombre'],direccion=request.POST['direccion'],email=request.POST['email'])

        sucur.save()
        return HttpResponse ("Sus datos fueron grabados")
    return render(request,"superapp/sucursalForm.html")



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


def buscarSucursal(request):
    return render(request, "superapp/buscarSucursal.html")

def buscar3(request):
    if request.GET['buscar3']:
        busqueda_avanzada2 = request.GET['buscar3']
        sucursales =Sucursales.objects.filter(nombre__icontains=busqueda_avanzada2)
        contexto3 ={"sucursales": sucursales}
        return render (request, "superapp/sucursales.html",contexto3)
    
    return HttpResponse("No se ingresaron datos")


def ofertaForm (request):
    if request.method == "POST":
        ofert = Ofertas(nombre = request.POST['nombre'],marca=request.POST['marca'],tipo_Empaque=request.POST['tipo_Empaque']
                         ,precio=request.POST['precio'])

        ofert.save()
        return HttpResponse ("Sus datos fueron grabados")
    return render(request,"superapp/ofertaForm.html")


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



def buscarOferta(request):
    return render(request, "superapp/buscarOferta.html")


def buscar4(request):
    if request.GET['buscar4']:
        busqueda_avanzada4 = request.GET['buscar4']
        ofertas =Ofertas.objects.filter(nombre__icontains=busqueda_avanzada4)
        contexto4 ={"ofertas": ofertas}
        return render (request, "superapp/ofertas.html",contexto4)
    
    return HttpResponse("No se ingresaron datos")


