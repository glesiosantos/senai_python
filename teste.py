nome_completo = input('Qual é o seu nome?')
ano_nascimento = input('Qual ano você nasceu?') 
ativo = True 
# print('Olá,', nome)

print(nome_completo.strip()) # remove espaço no final do texto

idade = 2026 - int(ano_nascimento)
print(f'Olá, {nome_completo} você tem {idade} ano(s)')
