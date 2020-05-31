"""
TheTeam URL Configuration

"""
#from django.contrib import admin
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

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
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
