categoria = int(input('Informe uma categoria: '))
qtd = int(input('Informe uma quantidade:'))
valor = 0
error = False

if categoria == 1 :
    valor = 10.
elif categoria == 2:
    valor = 18.
elif categoria == 3:
    valor = 23.
elif categoria == 4:
    valor = 26.
elif categoria == 5:
    valor = 31.
else:
    error = True
    print('Categoria invalida!')

if not error :
    print(f'Categoria {categoria}\nPreço Unit.: {valor}\nQuantidade: {qtd}\nTotal: {valor * qtd}')                