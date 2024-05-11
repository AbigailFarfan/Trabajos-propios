	Funcion SalarioDominical <- calcularSalarioDominical ( Domingos, HaberBasico )
		Si Domingos > 0 Entonces
			SalarioDominical <- Domingos*(HaberBasico/30)*2
		Sino
			SalarioDominical <- 0
		FinSi
	Fin Funcion
	
	Funcion ba <- calcularBonoAntiguedad ( añoingreso, añoactual, smn )
		ant <- añoactual - añoingreso
		Si ant >= 0 y ant <= 2  Entonces
			ba <- 0
		Sino
			Si ant > 2 y ant <= 5 Entonces
				ba <- 0.05 * 3 * smn
			Sino
				Si ant > 5 y ant <= 8 Entonces
					ba <- 0.11 * 3 * smn
				Sino
					Si ant > 8 y ant <= 11 Entonces
						ba <- 0.18 * 3 * smn
					Sino
						Si ant > 11 y ant <= 15 Entonces
							ba <- 0.26 * 3 * smn
						Sino
							Si ant > 15 y ant <= 20 Entonces
								ba <- 0.34 * 3 * smn
							Sino
								Si ant > 20 y ant <= 25 Entonces
									ba <- 0.42 * 3 * smn
								Sino
									Si ant < 25 Entonces
										ba <- 0.5 * 3 * smn
									Fin Si
								Fin Si
							Fin Si
						Fin Si
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	Fin Funcion
	
	Funcion afp <- calcularAFP (TotalIngresos, tipoempresa)
		Si tipoempresa = "Productiva" Entonces
			afp <- TotalIngresos * 0.1271
		Sino
			afp <- 0
		FinSi
	Fin Funcion
	
	Funcion anss <- calcularAporteSolidario (TotalIngresos)
		Si TotalIngresos < 13000 Entonces
			anss <- 0
		Sino
			Si TotalIngresos >= 13000 Y TotalIngresos <= 24999 Entonces
				anss <- (TotalIngresos - 13000) * 0.01
			Sino
				Si TotalIngresos >= 25000 Y TotalIngresos <= 34999 Entonces
					anss <- ((TotalIngresos - 13000) * 0.01) + ((TotalIngresos - 25000) * 0.05)
				Sino
					Si TotalIngresos >= 35000 Entonces
						anss <- ((TotalIngresos - 13000) * 0.01) + ((TotalIngresos - 25000) * 0.05) + ((TotalIngresos - 35000) * 0.1)
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	Fin Funcion
	
	Algoritmo boletadepagoFuncion
    Definir nombre, ci, cargo, mesactual, tipoempresa como caracter
    Definir añoingreso, añoactual, HaberBasico, BonoAlimentacion, BonoTransporte, ValesConsumo, SalarioDominical, smn, ant, ba, anss como real
    Definir Domingos, afp, TotalIngresos, TotalEgresos, LiquidoPagable como real
	
    Escribir "Ingrese el nombre del empleado:"
    Leer nombre
    Escribir "Ingrese la cedula de identidad del empleado:"
    Leer ci
    Escribir "Ingrese el cargo del empleado:"
    Leer cargo
    Escribir "Ingrese el año de ingreso a la empresa"
    Leer añoingreso
    Escribir "Ingrese el año actual"
    Leer añoactual
    Escribir "Ingrese el mes actual"
    Leer mesactual
    Escribir "Ingrese el tipo de empresa (Productiva o Servicios):"
    Leer tipoempresa
    Escribir "Ingrese el haber basico del empleado:"
    Leer HaberBasico
    Escribir "Ingrese el numero de domingos trabajados:"
    Leer Domingos
	
    BonoAlimentacion <- 60
    BonoTransporte <- 157.5
    ValesConsumo <- 88
    smn <- 2362
	
    SalarioDominical <- calcularSalarioDominical(Domingos, HaberBasico)
    ba <- calcularBonoAntiguedad(añoingreso, añoactual, smn)
	
    TotalIngresos <- HaberBasico + BonoAlimentacion + BonoTransporte + ValesConsumo + SalarioDominical + ba
	
    afp <- calcularAFP(TotalIngresos, tipoempresa)
	
    anss <- calcularAporteSolidario(TotalIngresos)
	
    TotalEgresos <- afp + anss
    LiquidoPagable <- TotalIngresos - TotalEgresos
	
    Escribir "-----------BOLETA DE PAGO -------------"
    Escribir "Nombre:", nombre
    Escribir "CI:", ci
    Escribir "Cargo:", cargo
    Escribir "Tipo de Empresa:", tipoempresa
    Escribir "Mes actual:", mesactual
    Escribir "Haber Basico:", HaberBasico, " Bs"
    Escribir "Bono de Alimentacion:", BonoAlimentacion, " Bs"
    Escribir "Bono de Transporte:", BonoTransporte, " Bs"
    Escribir "Bono de Antigüedad:", ba, " Bs"
    Escribir "Vales de Consumo:", ValesConsumo, " Bs"
    Escribir "Salario Dominical:", SalarioDominical, " Bs"
    Escribir "Total de Ingresos:", TotalIngresos, " Bs"
    Escribir "AFP:", afp, "Bs"
    Escribir "Aporte Nacional Solidario:", anss, " Bs"
    Escribir "Total Egresos:", TotalEgresos, " Bs"
    Escribir "Liquido Pagable:", LiquidoPagable, " Bs"
FinAlgoritmo
