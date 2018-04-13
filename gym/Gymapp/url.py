from django.urls import path 
from .views import *
from django.contrib.auth.models import User


urlpatterns = [
	path('', vista_horarios),	
	path('base/', vista_base, name = "vista_base"),	
    path('horarios/', vista_horarios, name = "vista_horarios"),
    path('usuario/', vista_usuario, name = "vista_usuario"),
    path('ejercicio/', vista_ejercicio, name = "vista_ejercicio"),
    path('recepcionista/', vista_recepcionista, name = "vista_recepcionista"),
    path('gym/', vista_gym, name = "vista_gym"),
    path('agregar_usuario/', vista_agregar_usuario, name = "vista_agregar_usuaario"),
    path('agregar_ejercicio/', vista_agregar_ejercicio, name = "vista_agregar_ejercicio"),
    path('ver_ejercicio/<int:id_prod>/', vista_ver_ejercicio, name = "vista_ver_ejercicio"),
    path('ver_usuario/<int:id_prod>/', vista_ver_usuario, name = "vista_ver_usuario"),
    path('ver_recepcionista/<int:id_prod>/', vista_ver_recepcionista, name = "vista_ver_recepcionista"),
    path('ver_gym/<int:id_prod>/', vista_ver_gym, name = "vista_ver_gym"),
    path('ver_horarios/<int:id_prod>/', vista_ver_horarios, name = "vista_ver_horarios"),

    path('login/', vista_login, name = "vista_login"),
    path('register/', vista_register, name = "vista_register"),
]
