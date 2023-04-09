from django import forms
from UserApp.models import CustomUser
from django.contrib.auth.forms import UserCreationForm



class UserLoginForm(forms.Form):

    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput())

class UserEditForm(forms.Form):
    avatar = forms.ImageField(required=False)
    username = forms.CharField(max_length=25, required=False)
    email = forms.EmailField(max_length=35, required=False)
    first_name = forms.CharField(max_length=25, required=False)
    last_name = forms.CharField(max_length=25, required=False)
    biografia = forms.CharField(max_length=200, required=False)

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', "email"]
    
class UserDeleteForm(forms.Form):

    password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')
    confirm = forms.BooleanField(initial=False  ,label='Me hago responsable',widget=forms.CheckboxInput())