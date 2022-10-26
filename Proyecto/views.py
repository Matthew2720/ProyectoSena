# hacer tabajos de controller!!
from django.http import HttpResponse
from django.template import Template , Context
from Proyecto.models import Cliente
from django.db import connection
from django.shortcuts import render
from django.contrib import messages

def index(request):
    return HttpResponse("hola mundo!") 

def listadoclientes(request):
    return render(request,'cliente/listaclientes.html',{})

def ClienteInsertar(request):
        if request.method == "POST":
            if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('edad') and request.POST.get('celular') and request.POST.get('fechanacimiento') and request.POST.get('email') and request.POST.get('genero') and request.POST.get('cedula'):
                Clientes = Cliente()
                Clientes.nombre = request.POST.get('nombre')
                Clientes.apellido = request.POST.get('apellido')
                Clientes.edad = request.POST.get('edad')
                Clientes.celular = request.POST.get('celular')
                Clientes.fechanacimiento = request.POST.get('fechanacimiento')
                Clientes.email = request.POST.get('email')
                Clientes.cedula = request.POST.get('cedula')
                Clientes.genero = request.POST.get('genero')
                insertar = connection.cursor() #alistar la sentencia a guardar
                insertar.execute("call insertarClientes('"+Clientes.nombre+"', '"+Clientes.apellido+"', '"+Clientes.edad+"', '"+Clientes.celular+"', '"+Clientes.fechanacimiento+"', '"+Clientes.email+"', '"+Clientes.genero+"','"+Clientes.cedula+"')")
                messages.success(request,"El Usuario ->" + Clientes.nombre + "se guardo con exito")
                return render(request,'cliente/insertar.html')
        else:
            return render(request,'cliente/insertar.html')












