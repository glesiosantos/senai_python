from models.pessoa import Pessoa
from models.pessoa_fisica import PessoaFisica
from models.pessoa_juridica import PessoaJuridica

def main():
    print('Inicializando Sistema')
    list = []

    jose = PessoaFisica('José Henrique','86 9.9998.6644', 'Rua das Tolipas','99988877766')
    senai = PessoaJuridica('Senai','86 9.9898.6655', 'Teresina Shopping', '66555222000100')

    list.append(jose)
    list.append(senai)

    for p in list:
        print(f'{p.exibir_dados()}')

if __name__ == "__main__":
    main() 