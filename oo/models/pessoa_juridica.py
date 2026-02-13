from models.pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, nome, telefone, endereco, cnpj):
        super().__init__(nome, telefone,endereco)
        self.cnpj = cnpj

    def exibir_dados(self):
        base = super().exibir_dados()    
        return f'{base} - CNPJ.: {self.cnpj}'