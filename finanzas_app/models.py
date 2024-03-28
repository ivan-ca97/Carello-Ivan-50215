from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class PerfilUsuario(models.Model):
    '''
    El perfil de usuario esta relacionado unívocamente con
    un User por defecto de Django. Con "on_delete" informo
    que de borrarse User, también debe borrarse el perfil
    '''
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

class ProveedorPagos(models.Model):
    nombre = models.CharField(max_length=255, unique=True, verbose_name='Nombre')
    tipo = models.CharField(max_length=50, choices={'banco': 'Banco', 'billetera_virtual': 'Billetera Virtual'}, verbose_name='Tipo de institución')
    pais = models.CharField(max_length=100, blank=True, null=True, verbose_name='País')
    paginaWeb = models.URLField(max_length=255, blank=True, null=True, verbose_name='Página Web')
    telefonoServicioAlCliente = models.CharField(max_length=20, blank=True, null=True, verbose_name='Teléfono servicio al cliente')

    aceptaCredito = models.BooleanField(verbose_name='Acepta Crédito')

    class Meta:
        verbose_name = "Proveedor de Pagos"
        verbose_name_plural = "Proveedores de Pagos"

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"
    
class Cuenta(models.Model):
    nombreAlias = models.CharField(max_length=100, blank=True, verbose_name='Alias de la cuenta')
    proveedorPagos = models.ForeignKey(ProveedorPagos, on_delete=models.CASCADE, verbose_name='Proveedor de pagos')
    reservas = models.FloatField()
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, verbose_name='Usuario')

    class Meta:
        verbose_name = "Cuenta"
        verbose_name_plural = "Cuentas"

    def __str__(self):
        if self.nombreAlias:
            return f"{self.nombreAlias}"
        else:
            return f"{self.usuario} - {self.proveedorPagos}"

class FormaDePago(models.Model):
    nombreAlias = models.CharField(max_length=100, blank=True, verbose_name='Alias de la forma de pago')
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, verbose_name='Usuario', null=True)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, verbose_name='Cuenta asociada', null=True)
    # Indica si es tarjeta de crédito porque necesita un tratamiento distinto
    #esCredito = models.BooleanField(verbose_name='Es tarjeta Crédito')

    class Meta:
        verbose_name = "Forma de pago"
        verbose_name_plural = "Formas de pago"

    def __str__(self):
        if self.nombreAlias:
            return f"{self.nombreAlias}"
        else:
            return f"Cuenta: {self.usuario} - {self.id}"

class Ingreso(models.Model):
    usuario     = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, verbose_name='Usuario', null=True)
    cuenta      = models.ForeignKey(Cuenta, on_delete=models.CASCADE, verbose_name='Cuenta asociada', null=True)
    monto       = models.FloatField(verbose_name='Monto')
    fecha       = models.DateField(verbose_name='Fecha', null=True)
    descripcion = models.CharField(max_length=300, blank=True, verbose_name='Descripción')

    class Meta:
        verbose_name = "Ingreso"
        verbose_name_plural = "Ingresos"

    def __str__(self):
        return f'{self.usuario} - ${self.monto}'

class Egreso(models.Model):
    usuario     = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, verbose_name='Usuario', null=True)
    formaDePago = models.ForeignKey(FormaDePago, on_delete=models.CASCADE, verbose_name='Forma de pago', null=True)
    monto       = models.FloatField(verbose_name='Monto')
    fecha       = models.DateField(verbose_name='Fecha', null=True)
    descripcion = models.CharField(max_length=300, blank=True, verbose_name='Descripción')

    class Meta:
        verbose_name = "Egreso"
        verbose_name_plural = "Egresos"