from django.shortcuts import render, redirect, get_object_or_404
from nombreApp.models import Producto
from .forms import ContactoForm, ProductoForm ,CustomUserCreationForm
from django.contrib.auth import authenticate, login


# Create your views here.
def plantilla(request):
    return render(request,'plantilla.html',{})

def Marcaa(request):
    mensaje = ""
    lista = {}
    item = {}
    #detecta si hay una solicitud 
    if request.method == "POST":
        #captura los valores entregados por los usuarios
        Id = int("0" + request.POST["txtId"]) #convertir en int
        nombre = request.POST["txtNombre"]
        #activo = "" + request.POST["chkActivo"]
        
        #detecta que boton presiono el usuario
        if 'btnGrabar' in request.POST:

            if Id < 1: #un nuevo registro
              Marca.objects.create(nombre = nombre, activo = activo)  #regitra los datos
             
            else:
                item = Marca.objects.get(pk = Id)
                item.nombre = nombre
                item.activo = activo 
                item.save() # guarda los cambios 
                item = {}

                mensaje = "Datos guardados"
        elif 'btnBuscar' in request.POST:   
            item = Marca.objects.get(pk = Id)

            if isinstance(item,Marca):
                mensaje = "registro no encontrado"
                item = {}
        elif 'btnListar' in request.POST:
           lista = Marca.objects.all()  
   
                 
        elif 'btnEliminar'in request.POST:   
            item = Marca.objects.get(pk = Id) #obtiene el registro segun id 

            if isinstance(item,Marca):
                item.delete()
                mensaje = "registro eliminado"
                item = {}

def agregar_producto(request):

    data = {

        'form': ProductoForm
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "Guardado correctamente"
        else:
            data["form"]= formulario
    
    return render(request, 'producto/agregar.html', data)

def listar_productos(request):
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }
    return render(request, 'producto/listar.html',data)

def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productos")
        data["form"] = formulario
            
    return render(request, 'producto/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar_productos")

def registro(request):
    data={
        'form':CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario= CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect(to="plantilla")
        data["form"] = formulario    

    return render(request,'registration/registro.html',data)     

def mono(request):
    return render(request,'mono.html',{})    

def palaa(request):
    return render(request,'pala.html',{})    

def macetafeaa(request):
    return render(request,'macetafea.html',{})    

def macenegraa(request):
    return render(request,'mace-negra.html',{})    

def rastrillo(request):
    return render(request,'rastrillo.html',{})        

def florosa(request):
    return render(request,'florosa.html',{})        
    
def tijerashojaa(request):
    return render(request,'tijerashoja.html',{})   

def floramarillas(request):
    return render(request,'floramarillas.html',{}) 


def tijerasbasicass(request):
    return render(request,'tijerasbasicas.html',{})     

def macetarara(request):
    return render(request,'macetarara.html',{})  

def bambu(request):
    return render(request,'bambu.html',{})      

def tierradehojas(request):
    return render(request,'tierradehojas.html',{}) 
      
def loginn(request):
    return render(request,'registration/login.html',{}) 


