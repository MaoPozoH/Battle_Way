from django.shortcuts import render

# Create your views here.


def base(request):
  return render(request, 'base.html')

def inicio(request):
  return render(request, 'inicio.html')

def acerca(request):
  return render(request, 'acerca.html') 

def productos(request):
#  productos = # obtener productos de la base de datos
    return render(request, 'productos.html')

# def producto(request, id):
#  producto = # obtener producto por id
#  return render(request, 'producto.html', {'producto': producto}) 

# def contacto(request):
#  return render(request, 'contacto.html')
