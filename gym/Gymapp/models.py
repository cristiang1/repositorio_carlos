from django.db import models

class horario(models.Model):
	jornada  = models.CharField(max_length = 30)

	def __str__(self):
		return self.jornada


class ejercicio(models.Model):
	nombre  = models.CharField(max_length = 30)
	repeticiones   = models.IntegerField()
	series   = models.IntegerField()


	def __str__(self):
		return self.nombre



class recepcionista(models.Model):
	nombre  = models.CharField(max_length = 30)
	


	def __str__(self):
		return self.nombre


class gym(models.Model):
	nombre  = models.CharField(max_length = 30)
	


	def __str__(self):
		return self.nombre


class usuario(models.Model):
	nombre  = models.CharField(max_length = 30)
	gym     = models.ManyToManyField(gym, null = True, blank = True)
	horarios	= models.ManyToManyField(horario, null = True, blank = True)
	ejercicio	= models.ManyToManyField(ejercicio, null = True, blank = True)
	recepcionista 	= models.ForeignKey(recepcionista, on_delete = models.CASCADE)



	def __str__(self):
		return self.nombre
