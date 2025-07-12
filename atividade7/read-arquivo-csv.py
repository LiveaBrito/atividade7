'''2- Crie um script em Python que leia um arquivo CSV e exiba os dados na tela.
O arquivo CSV deve conter informações de pessoas, com colunas:
- Nome, Idade e Cidade.'''

import csv

nome_arquivo = "pessoas.csv"

# Abrindo o arquivo para leitura
with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)

    cabecalho = next(leitor)
    print(f"Colunas: {cabecalho}")

    # Lê e exibe cada linha de dados
    print("\nDados")
    for linha in leitor:
        nome, idade, cidade = linha
        print(f"Nome: {nome}, idade: {idade}, Cidade: {cidade}")