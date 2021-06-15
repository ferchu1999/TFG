from django.contrib import admin
from .models import proveedoresModel, categorias, Comment


# Register your models here.


@admin.register(proveedoresModel)
class proveedoresAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ciudad', 'direccion', 'tfno', 'email']
    list_filter = ['created', 'nombre', 'categoria', 'ciudad']
    search_fields = ['nombre', 'ciudad', 'categoria']
    readonly_fields = ['created', 'updated']


@admin.register(categorias)
class categoriasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'created']
    list_filter = ['nombre', 'created']
    readonly_fields = ['created', 'updated']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'comentario', 'created', 'active')
    list_filter = ('active', 'created',)
    search_fields = ('nombre', 'comentario')
