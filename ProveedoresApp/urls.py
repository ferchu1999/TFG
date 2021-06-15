from django.urls import path
from . import views

urlpatterns = [
    path('proveedores/', views.proveedores, name='Proveedores'),
    path('proveedor/<slug:slug_proveedor>',
         views.proveedores_slug, name='Slug_proveedores'),
    path('altaproveedores/', views.crear_proveedores, name='alta_proveedores'),
]
