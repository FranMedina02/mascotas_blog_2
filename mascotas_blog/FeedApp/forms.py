from django import forms

class PostFormulario(forms.Form):
    #class = 'asd'
    title = forms.CharField(max_length=25)
    subtitle = forms.CharField(max_length=35)
    desc = forms.CharField(max_length=255)
    id_img = forms.ImageField()

