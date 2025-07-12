''' 1- Crie um script em Python que escreva dados em um arquivo CSV.
 O arquivo CSV deve conter informações de pessoas, com colunas:
- Nome, Idade e Cidade.'''

import csv

pessoas = [
    ["Anna", 25, "São Paulo"],
    ["Claudio", 17, "Rio Grande do Sul"],
    ["Vitória", 22, "Belo Horizonte"],
    ["Diego", 28, "Paraná"]
]

nome_arquivo = "pessoas.csv"

# Escrevendo no arquivo CSV
#ultilizei o comando ' mode="w" ' indica que o arquivo será aberto para escrita (write). Se ele já existir, será sobrescrito.

with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)

    escritor.writerow(["Nome", "Idade", "Cidade"])

    for pessoa in pessoas:
        escritor.writerow(pessoa)

    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")