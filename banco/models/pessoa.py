from models.endereco import Endereco
from models.contato import Contato

class Pessoa:
    def __init__(self, nome, endereco: Endereco):
        self.nome = nome
        self.endereco = endereco
        self._contatos:list[Contato] = []

    def mostrar_dados(self):
        info = f'Nome: {self.nome}\nEndereco:\n{self.endereco.logradouro} -  {self.endereco.bairro} - {self.endereco.cidade}/{self.endereco.estado}'
        infoContato = ''

        for contato in self._contatos:
             infoContato += f'{contato.ddd} {contato.numero}\n'

        return info+'\n'+infoContato     

    def add_contato(self, contato: Contato):
        self._contatos.append(contato)

    def to_dict(self):
        return {
            "nome": self.nome,
            "endereco": self.endereco.to_dict()
        }    
