from django import forms
from django.contrib.auth.models import User

class create_user(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class user_login_form(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(max_length= 40, widget=forms.PasswordInput)