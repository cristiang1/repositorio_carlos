
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Gymapp.url')),

    path('', include('web.urls')),
]
