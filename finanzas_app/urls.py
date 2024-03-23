from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', homeView, name = "home"),


    path('logout', Authentication.logOutView, name = "logout"),
    path('login', Authentication.logInView, name = "login"),
    path('signup', Authentication.signUpView, name = "signup"),

    path('perfil', perfilView, name = "perfil"),
]
