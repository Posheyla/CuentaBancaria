class CuentaBancaria:
    lista_cuenta=[]
    def __init__(self, tasa_interes = 0.01, balance = 0.0): 
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.lista_cuenta.append(self)

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrando una tarifa de ${}".format(self.balance))
            self.balance = 0
        return self

    def mostrar_info_cuenta(self):
        print("Balance: ${}".format(self.balance))
        return self

    def generar_interes(self):
        if self.balance>0:
            self.balance = self.balance + self.balance * self.tasa_interes
        else:
            print("No tiene dinero en su cuenta")
        return self
    
    @classmethod
    def imprimir_info_cuenta(cls):
        for i in cls.lista_cuenta:
            i.mostrar_info_cuenta()
