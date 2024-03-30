from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

# Creo un mixin para exigir superusuario
class SuperUserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        # De esta forma, si el usuario no es superusuario, no pasa la prueba
        return self.request.user.is_authenticated and self.request.user.is_superuser

    def handle_no_permission(self):
        # Paso mensaje de error y redirijo a home
        messages.error(self.request, "No tienes permiso de modificar esta información. Contáctese con un administrador.")
        return redirect(reverse('home'))