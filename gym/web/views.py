from Gymapp.models import *
from .serializer import *
from rest_framework import viewsets

class horario_viewset(viewsets.ModelViewSet):
	queryset = horario.objects.all()
	serializer_class = horario_serializer

class ejercicio_viewset(viewsets.ModelViewSet):
	queryset = ejercicio.objects.all()
	serializer_class = ejercicio_serializer

class recepcionista_viewset(viewsets.ModelViewSet):
	queryset = recepcionista.objects.all()
	serializer_class = recepcionista_serializer

class gym_viewset(viewsets.ModelViewSet):
	queryset = gym.objects.all()
	serializer_class = gym_serializer

class usuario_viewset(viewsets.ModelViewSet):
	queryset = usuario.objects.all()
	serializer_class = usuario_serializer