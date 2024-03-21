from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from .forms import *
# Create your views here.

def homeView(request):
    return render(request, 'base.html')





class Authentication:
    def logOutView(request):
        logout(request)
        return redirect(reverse_lazy('home'))


    def logInView(request):
        if request.method == "POST":
            form = LogInForm(request, data = request.POST)
                
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
                form.save()
                return redirect(reverse_lazy('home'))
            else:
                pass

            return render(request, 'authenticate.html', {'form': form, 'login_attempt': False, 'failed': True})
        else:
            signupForm = SignUpForm()
            return render(request, 'authenticate.html', {'form': signupForm, 'login_attempt': False})