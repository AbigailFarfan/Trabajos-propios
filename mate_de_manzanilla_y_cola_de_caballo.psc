Funcion preparar_mate_con_manzanilla_cola_de_caballo_y_miel ( cantidad_manzanilla, cantidad_cola_de_caballo )
	Escribir "¿Con qué tipo de edulcorante desea su mate?"
	Leer edulcorante
	Escribir "Introduciendo la bombilla dentro del poro."
	Escribir "Agregando una cucharadita de ", edulcorante, " al poro."
	Escribir "Agregando hierba al poro hasta la mitad."
	Escribir "¿Cuántas flores de manzanilla deseas agregar (entre 5 y 10)?"
	Leer cantidad_manzanilla
	Escribir "¿Cuántos palillos de cola de caballo deseas agregar (entre 5 y 10)?"
	Leer cantidad_cola_de_caballo
	Si cantidad_manzanilla >= 5 Y cantidad_manzanilla <= 10 Y cantidad_cola_de_caballo >= 5 Y cantidad_cola_de_caballo <= 10 Entonces
		Escribir "Agregando ", cantidad_manzanilla, " flores de manzanilla al poro."
		Escribir "Agregando ", cantidad_cola_de_caballo, " palillos de cola de caballo al poro."
	Sino
		Escribir "Por favor, ingresar una cantidad válida de manzanilla y cola de caballo."
	Fin Si
	
	Escribir "Agregando una cucharadita de ", edulcorante, " al poro."
	Escribir "Agregando agua caliente hasta que el poro quede lleno."
	Escribir "Su mate está listo"
Fin Funcion

Algoritmo mate_de_manzanilla_y_cola_de_caballo
Definir poro_y_bombilla_limpios, edulcorante Como Caracter
Definir cantidad_manzanilla, cantidad_cola_de_caballo Como Entero
Escribir "¿El poro y la bombilla están limpios? Escriba S para afirmar y N si es lo contrario"
Leer poro_y_bombilla_limpios
Segun poro_y_bombilla_limpios Hacer
	"S":
		preparar_mate_con_manzanilla_cola_de_caballo_y_miel(cantidad_manzanilla, cantidad_cola_de_caballo)
	"N":
		Escribir "Lavando el poro con agua"
		preparar_mate_con_manzanilla_cola_de_caballo_y_miel(cantidad_manzanilla, cantidad_cola_de_caballo)
	De Otro Modo:
		Escribir "Escriba un carácter válido"
Fin Segun
FinAlgoritmo

