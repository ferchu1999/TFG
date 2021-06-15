from django import forms
from .models import proveedoresModel, Comment


class crearProveedor(forms.ModelForm):
    class Meta:
        model = proveedoresModel
        fields = ['nombre', 'ciudad', 'direccion', 'tfno',
                  'email', 'web', 'productos', 'descripcion', 'categoria']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('nombre', 'comentario')
        widgets = {
            'comentario': forms.Textarea(attrs={'style': 'resize:none', 'rows': 10, 'cols': 30})
        }
