from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LogInForm(AuthenticationForm):
    username = forms.CharField(required = True, label="Nombre de usuario", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '',
        'type': 'text'
    }))
    password = forms.CharField(required = True, label="Contraseña", widget = forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': '',
        'type': 'password'
    }))



class SignUpForm(UserCreationForm):
    username = forms.CharField(required = True, label="Nombre de usuario", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '',
        'type': 'text'
    }))
    email = forms.EmailField(required = True, label="E-Mail", widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': '',
        'type': 'email'
    }))
    password1 = forms.CharField(required = True, label="Contraseña", widget = forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': '',
        'type': 'password'
    }))
    password2 = forms.CharField(required = True, label="Confirma Contraseña", widget = forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': '',
        'type': 'password'
    }))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

