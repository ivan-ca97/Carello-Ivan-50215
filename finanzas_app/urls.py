from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', homeView, name = "home"),


    path('logout', Authentication.logOutView, name = "logout"),
    path('login', Authentication.logInView, name = "login"),
    path('signup', Authentication.signUpView, name = "signup"),

    path('perfil', PerfilCBV.PerfilVer.as_view(), name = "perfil"),
    path('perfil_editar', PerfilCBV.PerfilUpdate.as_view(), name = "perfil_editar"),

    path('avatar', AvatarCBV.AvatarUpdate.as_view(), name='avatar'),

    path('cuentas', CuentaCBV.CuentasList.as_view(), name = "cuentas"),
    path('cuenta_crear', CuentaCBV.CuentaCrear.as_view(), name = "cuenta_crear"),
    path('cuenta_editar/<int:pk>/', CuentaCBV.CuentaUpdate.as_view(), name = "cuenta_editar"),
    path('cuenta_eliminar/<int:pk>/', CuentaCBV.CuentaDelete.as_view(), name = "cuenta_eliminar"),

    path('formas_de_pago', FormaDePagoCBV.FormaDePagoList.as_view(), name = "formas_de_pago"),
    path('forma_de_pago_crear', FormaDePagoCBV.FormaDePagoCrear.as_view(), name = "forma_de_pago_crear"),
    path('forma_de_pago_editar/<int:pk>/', FormaDePagoCBV.FormaDePagoUpdate.as_view(), name = "forma_de_pago_editar"),
    path('forma_de_pago_eliminar/<int:pk>/', FormaDePagoCBV.FormaDePagoDelete.as_view(), name = "forma_de_pago_eliminar"),

    path('ingresos', IngresoCBV.IngresoList.as_view(), name = "ingresos"),
    path('ingreso_crear', IngresoCBV.IngresoCrear.as_view(), name = "ingreso_crear"),
    path('ingreso_editar/<int:pk>/', IngresoCBV.IngresoUpdate.as_view(), name = "ingreso_editar"),
    path('ingreso_eliminar/<int:pk>/', IngresoCBV.IngresoDelete.as_view(), name = "ingreso_eliminar"),
    
    path('egresos', EgresoCBV.EgresoList.as_view(), name = "egresos"),
    path('egreso_crear', EgresoCBV.EgresoCrear.as_view(), name = "egreso_crear"),
    path('egreso_editar/<int:pk>/', EgresoCBV.EgresoUpdate.as_view(), name = "egreso_editar"),
    path('egreso_eliminar/<int:pk>/', EgresoCBV.EgresoDelete.as_view(), name = "egreso_eliminar"),









    path('proveedores_de_pagos', ProveedoresPagoCBV.ProveedoresPagoList.as_view(), name = "proveedores_de_pagos"),
    path('proveedor_de_pagos_crear', ProveedoresPagoCBV.ProveedoresPagoCrear.as_view(), name="proveedor_de_pagos_crear"),
    path('proveedor_de_pagos_eliminar/<int:pk>/', ProveedoresPagoCBV.ProveedoresPagoDelete.as_view(), name = "proveedor_de_pagos_eliminar"),
    path('proveedor_de_pagos_editar/<int:pk>/', ProveedoresPagoCBV.ProveedoresPagoUpdate.as_view(), name="proveedor_de_pagos_editar" ),
    #path('perfilusuario/<int:pk>/', MyModelDetailView.as_view(), name = "perfil"),
]
