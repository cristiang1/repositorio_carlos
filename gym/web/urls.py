from django.urls import path, include 
from rest_framework import routers 
from Gymapp.models import *
from web.views import *

router = routers.DefaultRouter()
router.register(r'horario', horario_viewset)

router.register(r'recepcionista', recepcionista_viewset)

router.register(r'ejercicios', ejercicio_viewset)

router.register(r'usuarios', usuario_viewset)

router.register(r'gym', gym_viewset)

urlpatterns = [
		
		path('api/', include(router.urls)),
		path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),




]
