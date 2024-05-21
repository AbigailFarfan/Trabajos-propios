DICCIONARIO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'CH': '----', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'Ñ': '--.--', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '"': '.-..-.',
    ' ': ' '
}

def Texto_a_Morse(texto):
    codigoMorse = []
    for caracter in texto.upper():
        if caracter in DICCIONARIO_MORSE:
            codigoMorse.append(DICCIONARIO_MORSE[caracter])
    return codigoMorse

DICCIONARIO_INVERSO_MORSE = {v: k for k, v in DICCIONARIO_MORSE.items()}

def Morse_a_Texto(codigoMorse):
    texto = []
    letras = codigoMorse.split('  ')
    for letra in letras:
        for simbolo in letra.split():
            if simbolo in DICCIONARIO_INVERSO_MORSE:
                texto.append(DICCIONARIO_INVERSO_MORSE[simbolo])
        texto.append(' ')
    return ''.join(texto).strip()

def DetectaryConvertir(cadena):
    if all(caracter in ['.', '-', ' ', '  '] for caracter in cadena):
        return Morse_a_Texto(cadena), 'morse'
    else:
        codigoMorse = Texto_a_Morse(cadena)
        return ' '.join(codigoMorse), 'text'

def Cuentas(cadena, tipodeConversion):
    if tipodeConversion == 'morse':
        listaCodigoMorse = cadena.split(' ')
        contadorPunto = sum(simbolo.count('.') for simbolo in listaCodigoMorse)
        contadorLinea = sum(simbolo.count('-') for simbolo in listaCodigoMorse)
        return listaCodigoMorse, contadorPunto, contadorLinea
    else:
        listaCodigoMorse = Texto_a_Morse(cadena)
        contadorPunto = sum(simbolo.count('.') for simbolo in listaCodigoMorse)
        contadorLinea = sum(simbolo.count('-') for simbolo in listaCodigoMorse)
        return listaCodigoMorse, contadorPunto, contadorLinea
    
def Almacenar_vector(listaCodigoMorse):
    vector = []
    for simbolo in listaCodigoMorse:
        vector.append(simbolo)
    return vector

cadena = input("Ingrese un texto en letras naturales o en código morse: ")
cadenaConvertida, tipodeConversion = DetectaryConvertir(cadena)
print(f"Convertido: {cadenaConvertida}")

if '.' in cadenaConvertida or '-' in cadenaConvertida:
    listaCodigoMorse = cadenaConvertida.split(' ')
else:
    listaCodigoMorse = Texto_a_Morse(cadena)

vector, contadorPunto, contadorLinea = Cuentas(cadena, tipodeConversion)
vectorAlmacenado = Almacenar_vector(vector)
print(f"Vector de código morse: {vectorAlmacenado}")
print(f"Puntos contados: {contadorPunto}")
print(f"Lineas contadas: {contadorLinea}")
