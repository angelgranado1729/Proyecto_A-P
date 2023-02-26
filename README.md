[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9312611&assignment_repo_type=AssignmentRepo)
# Proyecto Algoritmos y Programación 2223-1

Las instrucciones del proyecto las encontras en el siguiente link

https://docs.google.com/document/d/1oF0w3mygEI6X_Tx8RMZ_AMYmHQ5Zv84T_5ei2wOJbWY/edit?usp=sharing

# Proyecto: Qatar 2022 ⚽

Te han contratado para el desarrollo de un nuevo proyecto, un sistema para vender los tickets del mundial de fútbol Qatar 2022. Este sistema servirá para la venta de entradas, restaurantes, registrar asistencia y más.

El sistema consta de seis (6) módulos fundamentales:

-Gestión de partidos y estadios 
-Gestión de venta de entradas
-Gestión de asistencia a partidos
-Gestión de restaurantes
-Gestión de venta de restaurantes
-Indicadores de gestión (estadísticas)

**Nota:** Revise la información importante en observaciones.

## Gestión de partidos y estadios
	Este módulo permitirá a los usuarios administrar los equipos, enfrentamientos y los estadios en donde ocurrirán; para eso tendrás que tener en cuenta, que la información será dada a través de una API, (ver observaciones). Con esta información deberán desarrollar lo siguiente:

Registrar los equipos con la información proveniente de la API, es importante que se guarden los siguientes datos:
El nombre del país
Su código FIFA
El grupo en el que se encuentra
Registrar los estadios con la información  proveniente de la API, es importante que se guarden los siguientes datos:
El nombre
La Ubicación
Registrar los partidos con la información  proveniente de la API, es importante que se guarden los siguientes datos:
Equipo local (debe ser una referencia al objeto)
Equipo visitante (debe ser una referencia al objeto)
Fecha y hora
Estadio (debe ser una referencia al objeto)
Se deberá poder realizar la búsqueda de los partidos en función de los siguientes filtros:
Buscar todos los partidos de un país
Buscar todos los partidos que se jugarán en un estadio específico
Buscar todos los partidos que se jugarán en una fecha determinada
Gestión de venta de entradas
	Los organizadores del Qatar 2022 necesitarán un sistema para administrar las ventas de sus entradas; para esto necesitará solicitar los siguientes datos:

Datos del cliente:
Nombre del cliente
Cedula
Edad
Partido que desea comprar ticket (para esto se deberá mostrar toda la información de los partidos)
Tipo de entrada que desea comprar
Si es General: solo podrá ver el partido en su asiento y su precio es de $50
Si es VIP; podrá disfrutar del restaurante del estadio, es decir podrá adquirir productos de dicho restaurante. El precio de una entrada VIP es de $120
Luego el sistema deberá arrojarle un mapa del estadio, el cual el cliente podrá seleccionar un asiento, si el asiento está ocupado deberá notificarle al cliente que seleccione otro.
Por último le aparecerá el costo de la entrada según los siguientes casos:
si su cédula es un número vampiro su entrada tiene un 50% de descuento y se le notificara al cliente
Las entradas hay que sumarle el 16% del impuesto del valor agregado (IVA)
Luego deberá mostrar un mensaje indicando al cliente su asiento, costo (con información del subtotal, descuento, IVA y Total) y si desea proceder a pagar la entrada, de ser así, se ocupa el asiento y se muestra un mensaje de pago exitoso.

Gestión de asistencia a partidos
	En Qatar 2022, las entradas se compra con anticipación a los partidos, por lo que es posible que las personas no puedan asistir al partido, o que el por el contrario el partido esté lleno y se falsifiquen boletos; por tal razón el equipo de seguridad necesita de un módulo que les permita revisar si los boletos son válidos para ello deberá:

Validar la autenticidad del boleto con el código único del mismo
Si el boleto es auténtico deberá modificar la asistencia del partido
Un boleto puede ser falso si el código presentado no coincide con los códigos del sistema o si el código ya fue utilizado, es decir, un boleto con ese mismo código ya se usó para entrar al estadio 

	

Gestión de restaurantes
	En Qatar 2022 se necesitará un sistema para administrar su restaurante para sus clientes más importantes (VIP), esto debe tener  las siguientes funcionalidades:

Al tener que guardar el producto en su estructura de datos local, luego de haberla descargado del API, deberá guardar
Nombre del alimento/bebida.
Clasificación (alimento o bebida).
Si es bebida se debe registrar si es alcohólica o no. Si es alimento se debe guardar si es de empaque o de preparación.
Precio (se le deberá sumar el 16% del IVA).
Buscar productos por nombre, tipo, o rango de precio.


Gestión de venta de restaurantes
Para la venta en el restaurante se necesitará que el cliente ya haya comprado una entrada VIP, esto se validará con su cédula, si es así se procederá de la siguiente manera:
 Se guardan los datos del cliente:
Cedula.
Comida(s) que desee comprar
Si la edad el cliente es menor a 18 años no podrá comprar bebidas alcohólicas
Luego deberá mostrarle los productos que desea comprar con el monto total, siguiendo los siguientes casos:
Si la cédula es un número perfecto obtendrá un 15% de descuento.
Por último, si el cliente desea proceder con la compra, se le mostrará un mensaje de pago exitoso con un resumen de su compra donde se muestre el monto con su subtotal, descuento y total.
Se debe restar del inventario la cantidad de productos que el cliente compró


Indicadores de gestión (Estadísticas)

Toda empresa necesita evaluar su gestión y ver que le está funcionando y que no, para eso es importante un módulo de estadísticas que le indique a los organizadores de Qatar 2022 lo siguiente:

¿Cuál es el promedio de gasto de un cliente VIP en un partido (ticket + restaurante)?
Mostrar tabla con la asistencia a los partidos de mejor a peor, mostrando el nombre del partido (nombre de los equipos), estadio en donde se juega, boletos vendidos, personas que asistieron y la relación asistencia/venta
¿Cuál fue el partido con mayor asistencia?
¿Cuál fue el partido con mayor boletos vendidos?
Top 3 productos más vendidos en el restaurante.
Top 3 de clientes (clientes que más compraron boletos)
Realizar gráficos con dichas estadísticas con las librerías de mathplotlib o Bokeh (Bono).

Observaciones
Qatar 2022 posee una API en donde podrás obtener toda su información:
Documentación:https://github.com/Algoritmos-y-Programacion-2223-1/api-proyecto
Endpoints:
Equipos:https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json
Estadios:https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json
Partidos:https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json
La API tiene que funcionar como una opción de pre-cargado de datos antes de empezar a usar el programa, es decir esta opción crea el estado inicial del programa, posteriormente no se debe usar la API a menos que se quiera borrar los datos y cargar su estado inicial
Se deben usar los conceptos de programación orientado a objetos
Antes de realizar el código, es imperante que realicen un diagrama de clases y que la implementación de su proyecto sea uno a uno con el diagrama
Se evaluará que el código este comentado (docstring)
Se evaluará que el sistema contenga validaciones
Se deberán guardar datos en un archivo TXT para preservar los datos
El proyecto deberá ser entregado en Github Classroom a más tardar el 28 de noviembre de 2022 a las 11:59PM
