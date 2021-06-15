from django import forms
from .models import empresa, Comment


class crearEmpresa(forms.ModelForm):
    class Meta:
        model = empresa
        fields = ['tipo_empresa', 'nombre', 'ciudad', 'direccion',
                  'codigoPostal', 'tfno', 'email', 'logo_empresa', 'descripcion', 'CIF']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre de la empresa'}),
            'ciudad': forms.TextInput(attrs={'placeholder': 'Ciudad'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Dirección'}),
            'codigoPostal': forms.TextInput(attrs={'placeholder': '46010'}),
            'tfno': forms.TextInput(attrs={'placeholder': '643100291'}),
            'email': forms.TextInput(attrs={'placeholder': 'exampleemail@gmail.com'}),
            'descripcion': forms.Textarea(attrs={'placeholder': 'Descripción sobre tu empresa', 'style': 'resize:none'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'body': forms.Textarea(attrs={'style': 'resize:none', 'rows': 10, 'cols': 30})
        }
