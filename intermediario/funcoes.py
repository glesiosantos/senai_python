def nomeCompleto(primeiroNome, segundoNome='*'):
    return primeiroNome +' '+ segundoNome

primeiroNome = input('Informe o seu primeiro nome: ')
segundoNome = input('Informe o seu segundo nome: ')

nome = nomeCompleto(primeiroNome, segundoNome)

print(f'Seu nome completo é {nome}')
