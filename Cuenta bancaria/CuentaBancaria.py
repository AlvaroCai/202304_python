class CuentaBancaria:
    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance

    def deposito(self, cantidad):
        self.balance += cantidad
        return self

    def retiro(self, cantidad):
        self.balance -= cantidad
        return self

    def mostrar_info_cuenta(self):
        print("Tasa de Interes: ", self.tasa_interes)
        print("Balance: ", self.balance)

    def agregar_intereses(self):
        self.balance += self.balance * self.tasa_interes
        return self

# Crear la primera cuenta
cuenta1 = CuentaBancaria(0.05, 1000)
cuenta1.deposito(500).deposito(300).deposito(200).retiro(700).agregar_intereses().mostrar_info_cuenta()

# Crear la segunda cuenta
cuenta2 = CuentaBancaria(0.03, 500)
cuenta2.deposito(200).deposito(400).retiro(100).retiro(50).retiro(75).retiro(125).agregar_intereses().mostrar_info_cuenta()















