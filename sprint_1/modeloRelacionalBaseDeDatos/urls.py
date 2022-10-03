from unicodedata import name
from django.urls import path
from modeloRelacionalBaseDeDatos.views import EmpleadoView, EmpresasView, RolView, EmpleadoView, Reporte_contableView, UsuarioView
from modeloRelacionalBaseDeDatos.viewsFrontend import *
from modeloRelacionalBaseDeDatos.viewLogin import *


urlpatterns =[
    path('Empresas/', EmpresasView.as_view(), name= 'Listar'),
    path('Empresas/<str:idempresas>', EmpresasView.as_view(), name= 'Buscar'), #esta ruta nos sirve para consultar, agregar, actualizar y eliminar las empresas
    path('Empleado/', EmpleadoView.as_view(), name= 'Listar'),
    path('Empleado/<str:idempleado>', EmpleadoView.as_view(), name= 'Buscar'),
    path('Rol/',RolView.as_view(), name= 'Rol'),
    path('ReporteContable/',Reporte_contableView.as_view(), name= 'Reporte_contable'),
    path('', principal, name="index"),
    path('listaEmpresas/', listaEmpresas, name='lista'),
    path('consultarEmpresas/',consultarEmpresas, name='consultarId'),
    path('formempre/', formularioEmpresa, name="formulario"),
    path('guardarEmpresa/', guardarEmpresa, name='registrar'),
    path('prueba/', prueba, name='prueba'),
    path('cargarForm/<str:id_empresas>',cargarForm, name='formulario'),
    path('actualizarEmpresa/', actualizarEmpresa, name= 'actualizar'), #actualizar como se puso en el formulario formActualizar.html linea  16
    path('eliminarEmpresa/<str:id_empresas>', eliminarEmpresa, name='eliminar'),
    path('ingresar/', iniciarSesion, name= 'ingresar'),
    path('cerrar/', cerrarSesion, name='cerrar'),
    path('listaEmpresasUsu/', listaEmpresasUsu, name="listaEmpresasUsu"),
    path('consultarEmpresasUsu/', consultarEmpresasUsu, name="consultarEmpresasUsu"),
    path('Usuario_app/<str:idusuario>', UsuarioView.as_view(), name= 'UsuarioView'),
]

