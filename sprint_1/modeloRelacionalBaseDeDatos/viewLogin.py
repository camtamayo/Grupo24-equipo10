import email
from email import message
from django.shortcuts import render, redirect 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from modeloRelacionalBaseDeDatos.models import Usuario_app
from django.contrib import messages

#FUNCIÓN PARA INICIAR SESIÓN- LOGIN
def iniciarSesion(request):

    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre=form.cleaned_data.get("username")
            contrasenia=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre,password=contrasenia)
            if usuario is not None:
                try:
                    usu=Usuario_app.objects.get(email=usuario.email)
                    login(request,usuario)
                    return redirect('../listaEmpresasUsu')
                except Usuario_app.DoesNotExist:
                    if usuario.is_superuser:
                        login(request, usuario)
                        return redirect('../listaEmpresas')
                    else:
                        messages.success(request, f'Acceso Denegado')
            else:
                messages.success(request, f'El usuario no existe.')
    
        else:
            messages.success(request, f'Datos incorrectos.')

    form=AuthenticationForm()
    return render(request, "login.html", {"form":form})


#FUNCIÓN PARA CERRAR SESIÓN
def cerrarSesion(request):
    logout(request)
    return redirect('../') 