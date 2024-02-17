"""
URL configuration for battle_way project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from battle_way_app.views import base, inicio, acerca, productos  # Aquí se importan las vistas desde el archivo views.py de la aplicación battle_way_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base, name='base'),
    path('inicio/', inicio, name='inicio'),  # Asignando la vista inicio a la ruta raíz ''
    path('acerca/', acerca, name='acerca'),  # Asignando la vista acerca a la ruta 'acerca/'
    path('productos/', productos, name='productos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)