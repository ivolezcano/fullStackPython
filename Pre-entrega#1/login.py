import getpass

usuarios = {}

def registrarUsuarios():
    nombre = input('Ingrese su nombre de usuario: ')

    while True:
        contraseña = getpass.getpass('Ingrese su contraseña: ')
        confirmarContraseña = getpass.getpass('Confirme la contraseña: ')
        if contraseña == confirmarContraseña:
            usuarios[nombre] = contraseña
            print('*******************************')
            print('Usuario registrado con éxito !!')
            print('*******************************')
            break
        else:
            print('Las contraseñas no coinciden, intentelo de nuevo ')

def iniciarSesion():
    nombre = input('Ingrese su nombre de usuario: ')
    contraseña = getpass.getpass('Ingrese su contraseña: ')

    if nombre in usuarios and usuarios[nombre] == contraseña:
        print('********************')
        print('Inicio de sesión exitoso.')
        print(f'Bienvenido {nombre}')
        print('********************')
    else: 
        print('Nombre de usuario o contraseña incorrectos.')

# Bucle principal 

while True:
    print('\nOpciones:')
    print('1. Registrar Usuario')
    print('2. Iniciar sesión')
    print('3. Salir')

    opcion = input('Elije una opción: ')

    if opcion == '1':
        registrarUsuarios()
    elif opcion == '2':
        iniciarSesion()
    elif opcion == '3':
        print('Gracias, vuelva prontoS')
        break
    else:
        print(f'{opcion}, no es una opción válida. Vuelva a intentarlo.')