from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import PerfilUsuario, ProveedorPagos, Cuenta, FormaDePago, Ingreso, Egreso, Avatar


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']
        
        widgets = {
            'imagen': forms.FileInput(attrs={
                'class': 'form-control',
                'type': 'file',
            }),
        }

class CambiarPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(required = True, label="Contraseña actual", widget = forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': '',
        'type': 'password'
    }))
    new_password1 = forms.CharField(required = True, label="Contraseña nueva", widget = forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': '',
        'type': 'password'
    }))
    new_password2 = forms.CharField(required = True, label="Confirmar contraseña", widget = forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': '',
        'type': 'password'
    }))

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

class ProveedorPagosForm(forms.ModelForm):
    class Meta:
        model = ProveedorPagos
        fields = ['nombre', 'tipo', 'pais', 'paginaWeb', 'telefonoServicioAlCliente', 'aceptaCredito']
        
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-select',
                'type': 'text',
            }),
            'pais': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'paginaWeb': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'telefonoServicioAlCliente': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'aceptaCredito': forms.CheckboxInput(attrs={
                'class': 'form-check-label',
            }),
        }

class PerfilForm(forms.ModelForm):
    baseUsername = forms.CharField(required = True, label="Nombre de usuario", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
    }))

    baseEmail = forms.EmailField(required = True, label="E-Mail", widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'type': 'email'
    }))

    class Meta:
        model = PerfilUsuario
        fields = ["nombresPila", "apellido", "direccion", "telefono"]

        widgets = {
            'nombresPila': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
        }

class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['nombreAlias', 'proveedorPagos', 'reservas']
        
        widgets = {
            'nombreAlias': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'reservas': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'float',
            }),
            'proveedorPagos': forms.Select(attrs={
                'class': 'form-select',
                'type': 'text',
            }),
        }

class IngresoForm(forms.ModelForm):
    class Meta:
        model = Ingreso
        fields = ['cuenta', 'monto', 'fecha', 'descripcion']
        
        widgets = {
            'cuenta': forms.Select(attrs={
                'class': 'form-select',
                'type': 'text',
            }),
            'monto': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'float',
            }),
            # Debo agregar 'format' para que se cargue correctamente el
            # valor en el campo 'fecha' cuando edito una instancia
            'fecha': forms.DateInput(format='%Y-%m-%d', attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
        }
        
    def __init__(self, *args, **kwargs):
        '''
        El objetivo de esto es simplemente cambiar la lista de cuentas que
        recibe el formulario como opciones para que el usuario no pueda
        elegir cuentas ajenas
        '''
        super(IngresoForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.usuario:
            self.fields['cuenta'].queryset = Cuenta.objects.filter(usuario=self.instance.usuario)

class EgresoForm(forms.ModelForm):
    class Meta:
        model = Egreso
        fields = ['formaDePago', 'monto', 'fecha', 'descripcion']
        
        widgets = {
            'formaDePago': forms.Select(attrs={
                'class': 'form-select',
                'type': 'text',
            }),
            'monto': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'float',
            }),
            # Debo agregar 'format' para que se cargue correctamente el
            # valor en el campo 'fecha' cuando edito una instancia
            'fecha': forms.DateInput(format='%Y-%m-%d', attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
        }
        
    def __init__(self, *args, **kwargs):
        '''
        El objetivo de esto es simplemente cambiar la lista de cuentas que
        recibe el formulario como opciones para que el usuario no pueda
        elegir cuentas ajenas
        '''
        super(EgresoForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.usuario:
            self.fields['formaDePago'].queryset = FormaDePago.objects.filter(usuario=self.instance.usuario)

class FormaDePagoForm(forms.ModelForm):
    class Meta:
        model = FormaDePago
        fields = ['nombreAlias', 'cuenta']

        widgets = {
            'nombreAlias': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'cuenta': forms.Select(attrs={
                'class': 'form-select',
                'type': 'text',
            }),
        }

    def __init__(self, *args, **kwargs):
        '''
        El objetivo de esto es simplemente cambiar la lista de cuentas que
        recibe el formulario como opciones para que el usuario no pueda
        elegir cuentas ajenas
        '''
        super(FormaDePagoForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.usuario:
            self.fields['cuenta'].queryset = Cuenta.objects.filter(usuario=self.instance.usuario)