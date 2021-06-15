from django import forms


class formulario_contacto(forms.Form):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Nombre', 'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'class': 'form-control'}))
    tfno = forms.CharField(max_length=12, widget=forms.TextInput(
        attrs={'placeholder': 'Teléfono', 'class': 'form-control'}))
    mensaje = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Escríbenos tu mensaje', 'class': 'form-control', 'style': 'resize:none'}))
