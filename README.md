# Proyecto final Django Iván Carello

## Objetivo de la aplicación

La aplicación web se desarrolló con el objetivo de brindar una funcionalidad web capaz de brindar un servicio de registro de ingresos y egresos para organizar las finanzas personales, de forma intuitiva y flexible para adaptación de nuevas funcionalidades a futuro.

La idea del desarrollo surgió por razones personales, al utilizar planillas de excel para dicho propósito y pensar que quizás una aplicación sencilla que cumpla una función similar podría ser un proyecto interesante.

## Modelos
Los diversos modelos utilizados cumplen la funcion de caracterizar los movimientos que se registran y caracterizar al usuario.
### PerfilUsuario:
Este modelo se encarga de manejar la información de usuario, que no es la información que el modelo por defecto User necesita. Investigando online, encontré recomendaciones de implementar el perfil con una relacion OneToOne con User, por lo que decidí realizarlo de esta forma (Por más que contenga información que podría estar en User, decidí concentrar toda información adicional en PerfilUsuario). Además, todos los modelos que hagan referencia a un usuario en particular, tienen relacion con la PK de PerfilUsuario, no con User.

Se crea una instancia automáticamente cuando se crea una cuenta
### ProveedorPagos:
Este modelo representa entidades bancarias o billeteras virtuales, con información al respecto de las mismas. Se utiliza además para las intancias del modelo Cuenta. Cualquier usuario puede crear, modificar y borrar proveedores de pagos
### Cuenta:
Las cuentas son un modelo que representan las cuentas de los bancos/billeteras mencionadas anteriormente. Un ejemplo podría ser 'Caja de ahorros Galicia'. Cada usuario solo puede ver, modificar, crear y eliminar sus propias cuentas (Salvo que sea admin desde el panel admin). Las cuentas muestran la cantidad de dinero actualizada que hay en las mismas, que obtiene desde las intancias de Ingreso y Egreso. 
### Forma de pago:
Este modelo representa una forma de pago particular. Podría ser, por ejemplo, 'Transferencia MercadoPago'. Se utiliza para los egresos. Puede tener una cuenta asociada para el caso de pagos que extraen dinero automáticamente de una cuenta (Por ejemplo, transferencias, pago con tarjeta de débito)
### Ingresos:
Representa flujo positivo de dinero. Se debe informar, además del monto, la cuenta para representar dónde se recibió el ingreso. Además, se informa la fecha en la que se realizó y una descripción personalizada.
### Egresos:
Similar a los ingresos, se informa un monto, fecha y descripción, pero en lugar de necesitar una cuenta, utiliza una forma de pago. Si la forma de pago tiene una cuenta asociada, se modificará la reserva de esa cuenta de forma acorde.
### Avatar:
El modelo simplemente representa la imágen que corresponde a cada usuario.


## Funcionalidades no implementadas
Al plantear el proyecto se consideró la idea de manejar los datos con tarjeta de crédito, informando las tarjetas de cada usuario, resumenes, fechas de cierre y vencimiento... pero debido al incremento del alcance que ello representa y la complejidad, se decidió no implementarlo. 

## Superuser
Username: ivan

Contraseña: vivapython
