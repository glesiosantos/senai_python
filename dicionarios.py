tabelas = {
    "Abacaxi": 4.5,
    "Pera": 6.,
    "Uva": 18.5, 
    "Melancia": 3.5
}
# Imprimi a lista 
print(tabelas)

# imprimi somente as chaves
print(tabelas.keys())

# imprimi somente os valores
print(tabelas.values())

# imprimir valor especifico
print(tabelas['Abacaxi'])

tabelas.update(
    {
        "Maracujá": 5.35, 
        "Banana": 7.99 
    }
)

# tabelas.setdefault("Uva", 10.5)
tabelas.update({
    "Uva": 10.5
})

tabelas.setdefault("Manga", 11)

print(f'Atualizar tabela \n{tabelas}')