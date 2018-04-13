from django import forms
from .models import *

from django.contrib.auth.models import User

class agregar_usuario_form(forms.ModelForm):
	class Meta:
		model = usuario
		fields = '__all__'


class agregar_ejercicio_form(forms.ModelForm):
	class Meta:
		model = ejercicio
		fields = '__all__'




# USER-----------------------------------------

class register_form(forms.Form):
	username      = forms.CharField(widget=forms.TextInput())

	email      = forms.EmailField(widget=forms.TextInput())

	password_1      = forms.CharField(label='password', widget=forms.PasswordInput(render_value=False))

	password_2      = forms.CharField(label='confirmar password', widget=forms.PasswordInput(render_value=False))


	def clean_username (self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('nombre de usuario ya registrado')


	def clean_email (self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('correo electronico ya existe')


	def clean_password (self):
		password_1 = self.cleaned_data['password_1']
		password_2 = self.cleaned_data['password__2']
		
		if password_1==password__2:
			pass
		else:
			raise forms.ValidationError('PAswords no coinciden')


