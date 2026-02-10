nomeAluno = input('Qual o nome do aluno? ')
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3
situacao = ''
# se o aluno tiver média igual ou maior que 7 - Aprovado
# se o aluno tiver a média entre 5 a 7 - Recuperação
# abaixo de 5 estará reprovado

if media >= 7:
    situacao = 'aprovado'
elif media >= 5 and media < 7:
    situacao = 'recuperação'    
else:
    situacao = 'reprovado'

print(f'O aluno {nomeAluno} obteve a média de {media:.2f} e está {situacao}')
