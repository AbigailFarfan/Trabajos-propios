def calcular_salario_dominical(domingos, haber_basico):
    if domingos > 0:
        salario_dominical = domingos * (haber_basico / 30) * 2
    else:
        salario_dominical = 0
    return salario_dominical

def calcular_bono_antiguedad(año_ingreso, año_actual, smn):
    ant = año_actual - año_ingreso
    if 0 <= ant <= 2:
        ba = 0
    elif 2 < ant <= 5:
        ba = 0.05 * 3 * smn
    elif 5 < ant <= 8:
        ba = 0.11 * 3 * smn
    elif 8 < ant <= 11:
        ba = 0.18 * 3 * smn
    elif 11 < ant <= 15:
        ba = 0.26 * 3 * smn
    elif 15 < ant <= 20:
        ba = 0.34 * 3 * smn
    elif 20 < ant <= 25:
        ba = 0.42 * 3 * smn
    else:
        ba = 0.5 * 3 * smn
    return ba

def calcular_afp(total_ingresos, tipo_empresa):
    if tipo_empresa == "Productiva":
        afp = total_ingresos * 0.1271
    else:
        afp = 0
    return afp

def calcular_aporte_solidario(total_ingresos):
    if total_ingresos < 13000:
        anss = 0
    elif 13000 <= total_ingresos <= 24999:
        anss = (total_ingresos - 13000) * 0.01
    elif 25000 <= total_ingresos <= 34999:
        anss = ((total_ingresos - 13000) * 0.01) + ((total_ingresos - 25000) * 0.05)
    else:
        anss = ((total_ingresos - 13000) * 0.01) + ((total_ingresos - 25000) * 0.05) + ((total_ingresos - 35000) * 0.1)
    return anss

def boleta_de_pago_funcion():
    nombre = input("Ingrese el nombre del empleado: ")
    ci = input("Ingrese la cedula de identidad del empleado: ")
    cargo = input("Ingrese el cargo del empleado: ")
    año_ingreso = int(input("Ingrese el año de ingreso a la empresa: "))
    año_actual = int(input("Ingrese el año actual: "))
    mes_actual = input("Ingrese el mes actual: ")
    tipo_empresa = input("Ingrese el tipo de empresa (Productiva o Servicios): ")
    haber_basico = float(input("Ingrese el haber basico del empleado: "))
    domingos = int(input("Ingrese el numero de domingos trabajados: "))
    
    bono_alimentacion = 60
    bono_transporte = 157.5
    vales_consumo = 88
    smn = 2362
    
    salario_dominical = calcular_salario_dominical(domingos, haber_basico)
    ba = calcular_bono_antiguedad(año_ingreso, año_actual, smn)
    
    total_ingresos = haber_basico + bono_alimentacion + bono_transporte + vales_consumo + salario_dominical + ba
    
    afp = calcular_afp(total_ingresos, tipo_empresa)
    
    anss = calcular_aporte_solidario(total_ingresos)
    
    total_egresos = afp + anss
    liquido_pagable = total_ingresos - total_egresos
    
    print("-----------BOLETA DE PAGO -------------")
    print("Nombre:", nombre)
    print("CI:", ci)
    print("Cargo:", cargo)
    print("Tipo de Empresa:", tipo_empresa)
    print("Mes actual:", mes_actual)
    print("Haber Basico:", haber_basico, "Bs")
    print("Bono de Alimentacion:", bono_alimentacion, "Bs")
    print("Bono de Transporte:", bono_transporte, "Bs")
    print("Bono de Antigüedad:", ba, "Bs")
    print("Vales de Consumo:", vales_consumo, "Bs")
    print("Salario Dominical:", salario_dominical, "Bs")
    print("Total de Ingresos:", total_ingresos, "Bs")
    print("AFP:", afp, "Bs")
    print("Aporte Nacional Solidario:", anss, "Bs")
    print("Total Egresos:", total_egresos, "Bs")
    print("Liquido Pagable:", liquido_pagable, "Bs")

boleta_de_pago_funcion()
