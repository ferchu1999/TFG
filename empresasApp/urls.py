from django.urls import path
from . import views


urlpatterns = [
    path('empresas/', views.empresas, name='Empresas'),
    path('añadirempresa/', views.crear_empresa, name='añadirEmpresa'),
    path('empresa/<slug:slug_empresa>', views.empresas_slug, name='EmpresaSlug'),
]
