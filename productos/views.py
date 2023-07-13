from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Productos

def lista(request):
    productos = Productos.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'blogsite/index.html', context)

def agregar(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        producto = Productos(nombre=nombre, descripcion=descripcion, precio=precio)
        producto.save()
        return HttpResponseRedirect(reverse('lista'))
    else:
        return render(request, 'blogsite/agregar.html')
