from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.models import User

def vista_base(request):

	return render (request,'base.html', locals())

def vista_horarios(request):
	lista = horario.objects.all()
	
	return render (request,'horarios.html', locals())

def vista_usuario(request):
	listar = usuario.objects.all()
	return render (request,'usuario.html', locals())

def vista_ejercicio(request):
	listaE = ejercicio.objects.all()
	return render (request,'ejercicio.html', locals())

def vista_recepcionista(request):
	listaR = recepcionista.objects.all()
	return render (request,'recepcionista.html', locals())


def vista_gym(request):
	listaG = gym.objects.all()
	return render (request,'gym.html', locals())

# vistas agregar
def vista_agregar_usuario(request):
	if request.method == 'POST':
		formulario = agregar_usuario_form(request.POST,request.FILES)
		if  formulario.is_valid():
			prod = formulario.save(commit = False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect ('/usuario/')
	else:
		formulario = agregar_usuario_form()
	return render (request, 'agregar_usuario.html', locals())


def vista_agregar_ejercicio(request):
	if request.method == 'POST':
		formulario = agregar_ejercicio_form(request.POST,request.FILES)
		if  formulario.is_valid():
			prod = formulario.save(commit = False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect ('/ejercicios/')
	else:
		formulario = agregar_ejercicio_form()
	return render (request, 'agregar_ejercicio.html', locals())

# vistas ver 	


def vista_ver_ejercicio(request, id_prod):
	E = ejercicio.objects.get(id= id_prod)
	return render (request,'ver_ejercicio.html', locals())


def vista_ver_usuario(request, id_prod):
	U = usuario.objects.get(id= id_prod)
	return render (request,'ver_usuario.html', locals())


def vista_ver_recepcionista(request, id_prod):
	R = recepcionista.objects.get(id= id_prod)
	return render (request,'ver_recepcionista.html', locals())


def vista_ver_horarios(request, id_prod):
	H = horarios.objects.get(id= id_prod)
	return render (request,'ver_horarios.html', locals())


def vista_ver_gym(request, id_prod):
	G = gym.objects.get(id= id_prod)
	return render (request,'ver_gym.html', locals())


# login


def vista_login(request):
	
	return render (request,'login.html', locals())


# USER

def vista_register(request):
	formulario = register_form(	)
	if request.method == 'POST':
		formulario = register_form(request.POST,)
		if  formulario.is_valid():

			usuario = formulario.cleaned_data['username']
			correo = formulario.cleaned_data['email']
			password_1 = formulario.cleaned_data['password_1']
			password_2 = formulario.cleaned_data['password_2']

			u = User.objects.create_user(username=usuario, email=correo, password=password_1)
			u.save()
			return render(request, 'ok.html', locals())
		
		else:
			return render (request, 'register.html', locals())

	return render (request, 'register.html', locals())












