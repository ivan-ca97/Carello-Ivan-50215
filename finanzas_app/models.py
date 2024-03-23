from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class PerfilUsuario(models.Model):
    # El perfil de usuario esta relacionado unívocamente con
    # un User por defecto de Django. Con "on_delete" informo
    # que de borrarse User, también debe borrarse el perfil
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    nombresPila = models.CharField(max_length=100, blank=True, verbose_name='Nombre/s de pila')
    apellido = models.CharField(max_length=100, blank=True, verbose_name='Apellido')
    direccion = models.TextField(blank=True, verbose_name='Dirección')
    telefono = models.CharField(max_length=20, blank=True, verbose_name='Número de teléfono')

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return f"{self.apellido}, {self.nombresPila}"