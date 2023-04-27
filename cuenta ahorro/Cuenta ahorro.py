class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    def __str__(self):
        return f"cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: {self.balance}€"    
    def depositar(self, cantidad_ingreso):
        self.balance += cantidad_ingreso
        print("Ingreso aceptado")
    def retirar(self, cantidad_retirar):
        if self.balance >= cantidad_retirar:
            self.balance -= cantidad_retirar
            print("Reintegro realizado")
        else:
            print("No tienes sufiente dinero")

def crear_cliente():
    nombre_cliente = input("Ingrese su nombre: ")
    apellido_cliente = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombre_cliente, apellido_cliente, numero_cuenta)
    return cliente

def inicio():
    usuario = crear_cliente()
    print(usuario)
    opcion = 0

    while opcion != 'S':
        print('Escoje: Depositar (D), Retirar (R), o Salir (S)')
        opcion = input()
        
        if opcion == 'D':
            cantidad_ingresar = int(input("Cantidad a ingresar: "))
            usuario.depositar(cantidad_ingresar)
        elif opcion == 'R':
            cantidad_retirar = int(input("Cantidad a retirar: "))
            usuario.retirar(cantidad_retirar)
        print(usuario)
    print("Gracias por su visita")

inicio()
