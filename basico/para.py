lista = ('Morango', 'Pera', 'Uva', 'Laranja', 'Manga')

print('Usando FOR')
for fruta in lista:
    print(fruta)

count = 0

print('Usando WHILE')
while count < len(lista):
    print(lista[count])
    count = count + 1