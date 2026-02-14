class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.__saldo = 0

    def visualizarDadosConta(self):
        return f'Número Conta: {self.numero}\nTitular: {self.titular}\nSaldo: {self.__saldo}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if(valor <= self.__saldo):
            self.__saldo -= valor
            return True
             
        print(f'Saldo insuficiente! Seu saldo é de {self.__saldo:.2f}')
        return False    

    def tranferir(self, valor, destino):
        if self.sacar(valor):
            destino.depositar(valor)
            print('Tranferência realizada')
        else:
            print('Tranferência não realizada')    