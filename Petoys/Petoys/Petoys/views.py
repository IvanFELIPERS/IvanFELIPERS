"""from django.http import HttpResponse"""
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {
        # Context
    })

def inventarios(request):
    return render(request, 'inventarios.html', {
        # Context
    })

def mis_citas(request):
    return render(request, 'mis_citas.html', {
        # Context
    })
def mis_productos(request):
    return render(request, 'mis_productos.html', {
        # Context
    })
def ofertas(request):
    return render(request, 'ofertas.html', {
        # Context
    })
def pag_admi(request):
    return render(request, 'pag_admi.html', {
        # Context
    })
def pag_user(request):
    return render(request, 'pag_user.html', {
        # Context
    })
def productos(request):
    return render(request, 'productos.html', {
        # Context
    })
def recuperar_contrasena(request):
    return render(request, 'recuperar_contrasena.html', {
        # Context
    })
def registro(request):
    return render(request, 'registro.html', {
        # Context
    })
def venta(request):
    return render(request, 'venta.html', {
        # Context
    })