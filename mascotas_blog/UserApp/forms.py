from django import forms

class UserFormulario(forms.Form):

    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=35)
