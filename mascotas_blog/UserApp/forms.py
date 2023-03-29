from django import forms
from UserApp.models import CustomUser
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm



class UserLoginForm(forms.Form):

    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput())

class UserEditForm(forms.Form):

    username = forms.CharField(max_length=25, required=False)
    email = forms.EmailField(max_length=35, required=False)
    first_name = forms.CharField(max_length=25, required=False)
    last_name = forms.CharField(max_length=25, required=False)
    biografia = forms.CharField(max_length=200, required=False)

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', "email"]
    
'''
    def save(self, request):
        info = self.cleaned_data
        user = get_user_model().objects.create_user(
                                username = info['username'],
                                email = info['email'],
                                password = info['password'],
                                first_name = info['first_name'],
                                last_name = info['last_name'],
                                description = info['biografia']
                                )
        login(request,user)
'''