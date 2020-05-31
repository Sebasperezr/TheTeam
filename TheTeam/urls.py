"""TheTeam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
#from django.contrib import admin
from django.contrib import admin
from django.urls import path
from django.shortcuts import render

from rest_framework.routers import DefaultRouter
from Aplicaciones.encuesta.views import EncuestaViewSet
from Aplicaciones.actividad.views import ActividadViewSet
from Aplicaciones.empresa.views import EmpresaViewSet
from Aplicaciones.rol.views import RolViewSet
from Aplicaciones.usuario.views import UsuarioViewSet

router = DefaultRouter()
router.register(r'Aplicaciones.encuesta',EncuestaViewSet)
urlpatterns = router.urls

router = DefaultRouter()
router.register(r'Aplicaciones.actividad',ActividadViewSet)
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'Aplicaciones.empresa',EmpresaViewSet)
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'Aplicaciones.rol',RolViewSet)
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'Aplicaciones.usuario',UsuarioViewSet)
urlpatterns += router.urls


urlpatterns += [
    path('admin/', admin.site.urls),
]
