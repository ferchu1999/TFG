from django.contrib import admin
from .models import empresa, categoria_empresa, Comment

# Register your models here.


@admin.register(empresa)
class empresaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ciudad', 'direccion', 'tfno', 'email']
    list_filter = ['nombre', 'created', 'tipo_empresa', 'categoria']
    search_fields = ['nombre', 'ciudad', 'tipo_empresa', 'categoria']
    readonly_fields = ['created', 'updated']


@admin.register(categoria_empresa)
class categoria_empresaAdmin(admin.ModelAdmin):
    list_display = ['categoria']
    list_filter = ['categoria', 'created']
    readonly_fields = ['created', 'updated']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created', 'active')
    list_filter = ('active', 'created',)
    search_fields = ('name', 'body')
