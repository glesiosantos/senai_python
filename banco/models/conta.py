import json
from models.pessoa import Pessoa

class Conta:
    def __init__(self, numero, pessoa: Pessoa):
        self.numero = numero
        self.pessoa = pessoa
        self._saldo = 0

    def to_dict(self):
        return {
            "numero": self.numero,
            "pessoa": self.pessoa.to_dict()
        }
    
    def salvar_conta(self):
        try:
            with open('contas.json', 'r') as arquivo:
                contas = json.load(arquivo)
        except:
            contas = []
        
        contas.append(self.to_dict())

        with open('contas.json', 'w') as arquivo:
            json.dump(contas, arquivo, indent=4, ensure_ascii=False)

    def visualizarDadosConta(self):
        return f'Número Conta: {self.numero}\nTitular: {self.pessoa.nome}'
    
    def visualizarSaldoConta(self):
        return f'Seu saldo atual é de R$: {self._saldo:.2f}'

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if self._saldo >= valor:   
            self._saldo -= valor
            return True
        else: 
            print(f'Saldo insuficiente! Seu saldo é de {self._saldo:.2f}')
            return False

    def tranferir(self, valor, destino):
        if self.sacar(valor):
            destino.depositar(valor)
            print('Tranferência realizada')
        else:
            print('Tranferência não realizada')    