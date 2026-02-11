from endereco import Endereco

class Cliente :
    def __init__(self, nome, sobrenome, endereco: Endereco):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco

    def nomeCompleto(self):
        return self.nome +' '+ self.sobrenome    
