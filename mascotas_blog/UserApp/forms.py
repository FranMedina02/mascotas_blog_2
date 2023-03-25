from django import forms

class UserLoginForm(forms.Form):

    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=35)

class UserEditForm(forms.Form):

    username = forms.CharField(max_length=25, required=False)
    email = forms.EmailField(max_length=35, required=False)
    first_name = forms.CharField(max_length=25, required=False)
    last_name = forms.CharField(max_length=25, required=False)
    biografia = forms.CharField(max_length=200, required=False)



    
