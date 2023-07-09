class Usuario:
    def __init__(self, nombre, saldo_inicial):
        self.nombre = nombre
        self.saldo = saldo_inicial
        
    def hacer_deposito(self, cantidad):
        self.saldo += cantidad

    def hacer_retiro(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        else:
            return False
        
    def mostrar_balance_usuario(self):
        return self.saldo
    
# Crear las instancias de Usuario
usuario1 = Usuario("Juan", 1000)
usuario2 = Usuario("Maria", 500)
usuario3 = Usuario("Carlos", 200)

# Hacer los depósitos y el giro para el primer usuario
usuario1.hacer_deposito(500)
usuario1.hacer_deposito(200)
usuario1.hacer_deposito(300)
usuario1.hacer_retiro(400)

# Mostrar el balance actualizado del primer usuario
saldo_actual = usuario1.mostrar_balance_usuario()
print("El saldo actual de",usuario1.nombre, saldo_actual)

# Hacer los depósitos y giros para el segundo usuario
usuario2.hacer_deposito(1000)
usuario2.hacer_deposito(500)
usuario2.hacer_retiro(200)
usuario2.hacer_retiro(300)

# Mostrar el balance actualizado del segundo usuario
saldo_actual = usuario2.mostrar_balance_usuario()
print("El saldo actual de",usuario2.nombre, saldo_actual)

#Haz que el tercer usuario haga 1 depósito y 3 giros, y luego muestra sus balances
usuario3.hacer_deposito(2000)
usuario3.hacer_retiro(350)
usuario3.hacer_retiro(700)
usuario3.hacer_retiro(1000)
saldo_actual = usuario3.mostrar_balance_usuario()
print("El saldo actual de",usuario3.nombre, saldo_actual)



