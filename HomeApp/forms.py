from django import forms


class newsletter(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': 'example@example.com'}))
