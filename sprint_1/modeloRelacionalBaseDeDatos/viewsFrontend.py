#from urllib import request, response
import json
from urllib import response
from django.shortcuts import redirect, render 
from django.http import HttpResponse
import requests


def principal(request):
    return render(request, "index.html")

# FUNCIÓN PARA LISTAR LAS EMPRESAS EN EL FRONTEND 
def listaEmpresas(request):
    response=requests.get('http://127.0.0.1:8000/crud/Empresas/')
    empresas=response.json()
    print(empresas)
    return render(request, "empresas.html", empresas)

# FUNCIÓN PARA LISTAR LAS EMPRESAS EN EL FRONTEND POR ID 
def consultarEmpresas(request):
    dato= request.POST['id_empresas']   #El 'idempresas' es el que va en el input del formulario en empresas.html
    response=requests.get('http://localhost:8000/crud/Empresas/'+dato)
    empresa=response.json()
    print(empresa)
    return render(request, 'empresas.html',empresa)

# FUNCIÓN PARA EL FORMULARIO
def formularioEmpresa(request):
    return render(request, 'formempre.html')

# FUNCIÓN PARA CONECTAR DATOS DEL FORMULARIO FRONTEND CON BACKEND -GUARDA EMPRESA
def guardarEmpresa(request):
    datos={
        "id_empresas": request.POST['id_empresas'], #los datos entre los corchetes son los mismos que pusimos en el formulario con el name=""
        "nombre": request.POST['nombre'],
        "direccion":request.POST['direccion'],
        "ciudad": request.POST['ciudad'],
        "nit": request.POST['nit'],
        "sector_produc": request.POST['sector_produc'],
        "telefono": request.POST['telefono'],
        "fecha_creacion": request.POST['fecha_creacion']
    }
    requests.post('http://localhost:8000/crud/Empresas/',data=json.dumps(datos))
    return redirect('../listaEmpresas/')

# FUNCIÓN DE EJEMPLO PARA CONECTAR LUEGO EMPRESA CON EMPLEADO A TRAVÉS DE UN FORMULARIO DE SELECCIÓN MULTIPLE
def prueba(request):
    response=requests.get('http://localhost:8000/crud/Empresas/')
    empresas=response.json()
    print(empresas)
    return render(request, "prueba.html",empresas)

# FUNCIÓN PARA EL FORMULARIO formActualizar
def cargarForm(request, id_empresas):
    response=requests.get('http://localhost:8000/crud/Empresas/'+id_empresas)
    empresa=response.json()
    print(empresa)
    return render(request, 'formActualizar.html', empresa)


# FUNCIÓN PARA EL BOTON DE ACTUALIZAR LA EMPRESA
def actualizarEmpresa(request):
    codigo= request.POST['id_empresas']
    datos={
        "nombre": request.POST['nombre'],
        "direccion":request.POST['direccion'],
        "ciudad": request.POST['ciudad'],
        "nit": request.POST['nit'],
        "sector_produc": request.POST['sector_produc'],
        "telefono": request.POST['telefono'],
        "fecha_creacion": request.POST['fecha_creacion']
    }
    requests.put('http://localhost:8000/crud/Empresas/'+codigo, data=json.dumps(datos))
    return redirect('../listaEmpresas/')


# FUNCIÓN PARA EL BOTÓN DE ELIMINAR LA EMPRESA
def eliminarEmpresa(request, id_empresas):
    response=requests.delete('http://localhost:8000/crud/Empresas/'+id_empresas)
    empresa=response.json()
    print(empresa)
    return redirect('../listaEmpresas/')


#_________________________
 

# FUNCIÓN PARA LISTAR LAS EMPRESAS EN EL FRONTEND 

def listaEmpresasUsu(request):
    response=requests.get('http://127.0.0.1:8000/crud/Empresas/')
    empresas=response.json()
    print(empresas)
    return render(request, "usuarioApp.html", empresas)

# FUNCIÓN PARA LISTAR LAS EMPRESAS EN EL FRONTEND POR ID 
def consultarEmpresasUsu(request):
    dato= request.POST['id_empresas']   #El 'idempresas' es el que va en el input del formulario en empresas.html
    response=requests.get('http://localhost:8000/crud/Empresas/'+dato)
    empresa=response.json()
    print(empresa)
    return render(request, 'usuarioApp.html',empresa)
