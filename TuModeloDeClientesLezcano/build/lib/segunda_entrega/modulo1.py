class Cliente:
    def __init__(self, nombre, apellido,  edad, saldo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.saldo = saldo

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre} {self.apellido}\nEdad: {self.edad} años\nSaldo: ${self.saldo}\n")

    def realizar_compra(self, costo, producto, lugar):
        if costo<= self.saldo:
            self.saldo -= costo
            print(f"Compra realizada. Nuevo saldo: ${self.saldo}\n")
            print(f"COMPRA REALIZADA✔️ \n_Detalles de la compra_\nProducto: {producto} ${costo} Lugar: {lugar}\n")
        else:
            print("Fondos insuficientes para realizar la compra.")

    def __str__(self):
        return f"*NUEVO USUARIO CREADO*\nCliente: {self.nombre}, Edad: {self.edad}, Saldo: ${self.saldo}"