from segunda_entrega.modulo1 import Cliente
from segunda_entrega.modulo2 import *

while True:
    print('\nOpciones:')
    print('1. Registrar Usuario')
    print('2. Iniciar sesión')
    print('3. Mostrar Usuarios registrados')
    print('4. Salir')

    opcion = input('Elije una opción: ')

    if opcion == '1':
        registrarUsuarios(usuarios)
    elif opcion == '2':
        usuario_iniciado = iniciarSesion(usuarios)
        if usuario_iniciado is not None:
            nuevo_cliente = Cliente(usuario_iniciado['nombre'], usuario_iniciado['apellido'], int(usuario_iniciado['edad']), usuario_iniciado['saldo'])
            print(f'Bienvenido, {usuario_iniciado["nombre"]} {usuario_iniciado["apellido"]}.')
            while True:
                print('\nAcciones:')
                print('1. Mostrar información')
                print('2. Realizar compra')
                print('3. Consultar saldo')
                print('4. Cerrar sesión')

                accion = input('¿Qué deseas hacer?: ')

                if accion == '1':
                    nuevo_cliente.mostrar_informacion()
                elif accion == '2':
                    costo = int(input('Ingrese monto del producto: '))
                    producto = input('Ingrese el nombre del producto: ')
                    lugar = input('Ingrese el lugar de compra: ')
                    nuevo_cliente.realizar_compra(costo, producto, lugar)
                    usuario_iniciado['saldo'] = nuevo_cliente.saldo
                elif accion == '3':
                    print(f'Saldo actual: ${nuevo_cliente.saldo}')
                elif accion == '4':
                    print('Sesión cerrada. Hasta luego.')
                    break
                else:
                    print(f'{accion}, no es una opción válida. Vuelva a intentarlo.')
    elif opcion == '3':
        mostrarUsuarios(usuarios)
    elif opcion == '4':
        print('Hasta luego, vuelva pronto !')
        break
    else:
        print(f'{opcion}, no es una opción válida. Vuelva a intentarlo.')