"""Petoys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('inventarios/', views.inventarios, name='inventarios'),
    path('mis_citas/', views.mis_citas, name='mis_citas'),
    path('mis_productos/', views.mis_productos, name='mis_productos'),
    path('ofertas/', views.ofertas, name='ofertas'),
    path('pag_admi/', views.pag_admi, name='pag_admi'),
    path('pag_user/', views.pag_user, name='pag_user'),
    path('productos/', views.productos, name='productos'),
    path('recuperar_contrasena/', views.recuperar_contrasena, name='recuperar_contrasena'),
    path('registro/', views.registro, name='registro'),
    path('venta/', views.venta, name='venta')
]
