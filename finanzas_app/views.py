from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *
# Create your views here.

def homeView(request):
    return render(request, 'base.html')



class EditarPerfilForm(forms.ModelForm):
    nombresPila = forms.CharField(max_length=100, required=False, label="Editar Nombre", widget = forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'aria-label': 'EditarNombre',
        'aria-describedby': 'btnEditarNombre',
        'value': None,
    }))
    apellido = forms.CharField(max_length=100, required=False, label="Editar Apellido", widget = forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'aria-label': 'EditarApellido',
        'aria-describedby': 'btnEditarApellido',
    }))
    direccion = forms.CharField(max_length=100, required=False, label="Editar Dirección", widget = forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'aria-label': 'EditarDirección',
        'aria-describedby': 'btnEditarDirección',
    }))
    telefono = forms.CharField(max_length=100, required=False, label="Editar Telefono", widget = forms.CheckboxInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'aria-label': 'EditarTelefono',
        'aria-describedby': 'btnEditarTelefono',
    }))

    nombresPilaEditar = forms.BooleanField(required=False, initial=False, widget = forms.CheckboxInput(attrs={
        'type': 'submit',
        'class': 'btn btn-primary',
        'value': 'Editar',
    }))

    apellidoEditar = forms.BooleanField(required=False, initial=False, widget = forms.CheckboxInput(attrs={
        'type': 'submit',
        'class': 'btn btn-primary',
        'value': 'Editar',
    }))

    emailEditar = forms.BooleanField(required=False, initial=False, widget = forms.CheckboxInput(attrs={
        'type': 'submit',
        'class': 'btn btn-primary',
        'value': 'Editar',
    }))

    telefonoEditar = forms.BooleanField(required=False, initial=False, widget = forms.CheckboxInput(attrs={
        'type': 'submit',
        'class': 'btn btn-primary',
        'value': 'Editar',
    }))

    direccionEditar = forms.BooleanField(required=False, initial=False, widget = forms.CheckboxInput(attrs={
        'type': 'submit',
        'class': 'btn btn-primary',
        'value': 'Editar',
    }))

    class Meta:
        model = PerfilUsuario
        fields = ["nombresPila", "apellido", "direccion", "telefono"]

def editarCampoPerfil(request, campoNombre, replyForm, inputForm):
    # Veo el estado de habilitación de edición de cada campo
    campoHabilita = campoNombre + 'Editar'

    botonNombre = request.POST.get(campoHabilita)
    if botonNombre == 'Editar':
        replyForm.initial[campoHabilita] = True
        replyForm.fields[campoHabilita].widget.attrs['value'] = 'Enviar'

        #replyForm.fields[campoNombre].widget.attrs['value'] = request.user.perfilusuario.nombresPila
        replyForm.fields[campoNombre].widget.attrs['value'] = getattr(request.user.perfilusuario, campoNombre)
    elif botonNombre == 'Enviar':
        setattr(request.user.perfilusuario, campoNombre, inputForm.cleaned_data.get(campoNombre))
        request.user.perfilusuario.save()


@login_required(login_url='/accounts/login/')
def perfilView(request):
    if request.method == 'POST':
        print(request.POST)
        # Obtengo el formulario que recibe el servidor
        inputForm = EditarPerfilForm(request.POST)
        if inputForm.is_valid():
            replyForm = EditarPerfilForm(instance=request.user.perfilusuario)

            print('Editar campo...')
            editarCampoPerfil(request, 'nombresPila', replyForm, inputForm)
            editarCampoPerfil(request, 'apellido', replyForm, inputForm)
            editarCampoPerfil(request, 'direccion', replyForm, inputForm)
            editarCampoPerfil(request, 'telefono', replyForm, inputForm)

            contexto = {'perfilUsuario': request.user.perfilusuario, 'form': replyForm}
            return render(request, 'user_information.html', contexto)
        else:
            print('Errors:', inputForm.errors)
            nombresPilaEditar = inputForm.cleaned_data.get('nombresPilaEditar')

            if nombresPilaEditar:
                print("Nombre on!!")
            else:
                print("Nombre off!!")
    
    else:
        formVisibilidad = EditarPerfilForm(instance=request.user.perfilusuario)
        contexto = {'perfilUsuario': request.user.perfilusuario, 'form': formVisibilidad}
        return render(request, 'user_information.html', contexto)

@login_required(login_url='/accounts/login/')
def perfilViewww(request):

    if request.method == 'POST':

        inputForm = EditarPerfilForm(request.POST)
        if inputForm.is_valid():

            replyForm = EditarPerfilForm()

            botonNombre = request.POST.get('BotonNombre')
            if botonNombre == 'True':
                print("Holaaaa")
                replyForm.initial['nombreOn'] = True
                replyForm.fields['nombresPila'].widget.attrs['placeholder'] = request.user.perfilusuario.nombresPila
        

            print('reply: ', inputForm.cleaned_data.get('nombresPila'))
            request.user.perfilusuario.nombresPila = inputForm.cleaned_data.get('nombresPila')
            request.user.perfilusuario.save()
            print(inputForm.cleaned_data.get('nombresPila'), "Saving...")
            print(request.user.perfilusuario.nombresPila)

            contexto = {'perfilUsuario': request.user.perfilusuario, 'form': replyForm}
            return render(request, 'user_information.html', contexto)
        else:
            print('Errors:', inputForm.errors)
            nombreOn = inputForm.cleaned_data.get('nombreOn')

            if nombreOn:
                print("Nombre on!!")
            else:
                print("Nombre off!!")


    formVisibilidad = EditarPerfilForm()
    contexto = {'perfilUsuario': request.user.perfilusuario, 'form': formVisibilidad}
    return render(request, 'user_information.html', contexto)



class Authentication:
    def logOutView(request):
        logout(request)
        return redirect(reverse_lazy('home'))


    def logInView(request):
        if request.method == "POST":
            form = LogInForm(request, data=request.POST)
                
            if form.is_valid():
                userName        = form.cleaned_data.get('username')
                userPassword    = form.cleaned_data.get('password')
                
                user = authenticate(request, username=userName, password=userPassword)
                if user is not None:
                    login(request, user)
                    return redirect(reverse_lazy('home'))


                print("...", userName)
                print("...", userPassword)
                print("Errors...", form.errors)

            return render(request, 'authenticate.html', {'form': form, 'login_attempt': True, 'failed': True})

        else:
            logInForm = LogInForm()
            return render(request, 'authenticate.html', {"form": logInForm, "login_attempt": True})


    def signUpView(request):

        if request.method == "POST":
            form = SignUpForm(request.POST)

            if form.is_valid():
                nuevoUsuario = form.save()
                PerfilUsuario(usuario = nuevoUsuario).save()
                login(request, nuevoUsuario)
                return redirect(reverse_lazy('home'))
            else:
                pass

            return render(request, 'authenticate.html', {'form': form, 'login_attempt': False, 'failed': True})
        else:
            signupForm = SignUpForm()
            return render(request, 'authenticate.html', {'form': signupForm, 'login_attempt': False})
    