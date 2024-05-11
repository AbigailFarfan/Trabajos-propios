import sqlite3

def conectar_bd():
    return sqlite3.connect('usuarios.db')

def crear_tabla_usuarios():
    with conectar_bd() as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT NOT NULL UNIQUE,
                contrasena TEXT NOT NULL,
                rol TEXT NOT NULL
            )
        ''')

def inicializar_bd():
    crear_tabla_usuarios()
    
def registro():
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo electrónico: ")
    contrasena = input("Ingrese su contraseña: ")
    rol = input("Ingrese su rol (estudiante/docente): ")

    with conectar_bd() as conexion:
        cursor = conexion.cursor()
        cursor.execute('INSERT INTO usuarios (nombre, correo, contrasena, rol) VALUES (?, ?, ?, ?)', (nombre, correo, contrasena, rol))
        conexion.commit()
    print("¡Registro exitoso!")

def login():
    correo = input("Ingrese su correo electrónico: ")
    contrasena = input("Ingrese su contraseña: ")

    with conectar_bd() as conexion:
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE correo = ? AND contrasena = ?', (correo, contrasena))
        usuario = cursor.fetchone()

    if usuario:
        print("¡Inicio de sesión exitoso!")
        return usuario
    else:
        print("Correo o contraseña incorrectos")
        return None

def perfil(usuario):
    if usuario:
        print(f"Bienvenido, {usuario[1]}")
        print("=== Perfil ===")
        print(f"Correo electrónico: {usuario[2]}")
        print(f"Rol: {usuario[4]}")
    else:
        print("Debe iniciar sesión primero")
        
def main():
    inicializar_bd()

    while True:
        print("\n=== Menú ===")
        print("1. Registro")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registro()
        elif opcion == "2":
            usuario = login()
            if usuario:
                perfil(usuario)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
