from models.pessoa_fisica import PessoaFisica
from models.pessoa_juridica import PessoaJuridica
from models.pessoa import Pessoa

pessoasList = []

def formPessoaFisica():
    nome = input('Informe nome do cliente: ')
    telefone = input('Informe o telefone: ')
    cpf = input('Informe CPF do cliente: ')
    pessoa = PessoaFisica(nome,telefone,cpf)
    addPessoaList(pessoa)

def formPessoaJuridica():
    nome = input('Informe Razão Social do cliente: ')
    telefone = input('Informe o telefone: ')
    cnpj = input('Informe CNPJ do cliente: ')
    pessoa = PessoaJuridica(nome,telefone,cnpj)
    addPessoaList(pessoa)

def addPessoaList(pessoa: Pessoa):
    pessoasList.append(pessoa)

def carregarPessoaCadastradas():
    if not pessoasList:
        print("Nenhum cliente cadastrado")
        return
    
    for pessoa in pessoasList:
        print(pessoa.exibir_dados())