class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def obtener_saldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(
                f"Depósito de ${cantidad} realizado. Saldo actual: ${self.__saldo}"
            )
        else:
            print("La cantidad debe ser mayor que cero.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(
                f"Retiro de ${cantidad} realizado. Saldo actual: ${self.__saldo}"
            )
        else:
            print("Fondos insuficientes o cantidad inválida.")


# Crear una instancia de la cuenta bancaria
mi_cuenta = CuentaBancaria("Alice", 1000)

# Interactuar con la cuenta utilizando métodos encapsulados
print(f"Saldo actual: ${mi_cuenta.obtener_saldo()}")
mi_cuenta.depositar(500)
mi_cuenta.retirar(200)
