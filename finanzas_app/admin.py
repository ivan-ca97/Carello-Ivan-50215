from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(PerfilUsuario)
admin.site.register(ProveedorPagos)
admin.site.register(Cuenta)
admin.site.register(FormaDePago)
admin.site.register(Ingreso)
admin.site.register(Egreso)