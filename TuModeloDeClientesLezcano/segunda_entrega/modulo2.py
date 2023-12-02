import getpass
from modulo1 import Cliente

usuarios = {}

def registrarUsuarios(baseDatos):
    nombre = input('Ingrese su nombre de usuario: ')

    while True:
        contraseña = getpass.getpass('Ingrese su contraseña: ')
        confirmarContraseña = getpass.getpass('Confirme la contraseña: ')
        if contraseña == confirmarContraseña:
            edad = input('Ingrese su edad: ')
            saldo = 50000
            baseDatos[nombre] = {'contraseña': contraseña, 'apellido': input('Ingrese su apellido: '), 'edad': edad, 'saldo': saldo}
            print('*******************************')
            print('Usuario registrado con éxito !!')
            print('*******************************')
            break
        else:
            print('Las contraseñas no coinciden, intentelo de nuevo ')

def iniciarSesion(baseDatos):
    nombre = input('Ingrese su nombre de usuario: ')
    contraseña = getpass.getpass('Ingrese su contraseña: ')

    if nombre in usuarios and baseDatos[nombre]['contraseña'] == contraseña:
        print('********************')
        print('Inicio de sesión exitoso.')
        # print(f'Bienvenido {nombre}')
        print('********************')
        return {'nombre': nombre, 'apellido': baseDatos[nombre]['apellido'], 'edad':baseDatos[nombre]['edad'], 'saldo':baseDatos[nombre]['saldo']}
    else: 
        print('Nombre de usuario o contraseña incorrectos.')
        return None

def mostrarUsuarios(baseDatos):
    if not baseDatos:
        print('Aún no hay usuarios registrados.')
    else: 
        print('**********************')
        print('USUARIOS REGISTRADOS :')
        for usuario, detalles in baseDatos.items():
            print(f'Usuario: {usuario}, Contraseña: {detalles["contraseña"]}, Apellido: {detalles["apellido"]}, Edad: {detalles["edad"]}')

# # Bucle principal 

# while True:
#     print('\nOpciones:')
#     print('1. Registrar Usuario')
#     print('2. Iniciar sesión')
#     print('3. Mostrar Usuarios registrados')
#     print('4. Salir')

#     opcion = input('Elije una opción: ')

#     if opcion == '1':
#         registrarUsuarios(usuarios)
#     elif opcion == '2':
#         iniciarSesion(usuarios)
#     elif opcion == '3':
#         mostrarUsuarios(usuarios)
#     elif opcion == '4':
#         print('Hasta luego, vuelva pronto !')
#         break
#     else:
#         print(f'{opcion}, no es una opción válida. Vuelva a intentarlo.')