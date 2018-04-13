from rest_framework import serializers
from Gymapp.models import *

class horario_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = horario
		fields = ('url','jornada',)	

class recepcionista_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = recepcionista 
		fields = ('url','nombre')

class ejercicio_serializer(serializers.HyperlinkedModelSerializer):
	class Meta: 
		model = ejercicio
		fields = ('url','series','repeticiones','nombre')

class gym_serializer(serializers.HyperlinkedModelSerializer):
	class Meta: 
		model = gym 
		fields = ('url','nombre')

class usuario_serializer(serializers.HyperlinkedModelSerializer):
	class Meta: 
		model = usuario
		fields = ('url','nombre','gym','horarios','ejercicios','recepcionista')