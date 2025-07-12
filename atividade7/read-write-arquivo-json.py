'''3- Crie um script em Python que leia e escreva dados em um arquivo JSON.
 O arquivo JSON deve conter informações de uma pessoa, com campos:
- Nome, Idade e Cidade.'''

import json

pessoa = {
    "Nome" : "Maria",
    "Idade" : 27,
    "Cidade" : "Salvador"
}

nome_arquivo = "pessoa.json"

#Escrita no arquivo json
with open(nome_arquivo, mode="w", encoding="utf-8") as arquivo_json:
    json.dump(pessoa, arquivo_json, ensure_ascii=False, indent=4)

    print(f"Dados salvos no arquivo '{nome_arquivo}' com sucesso!")

# Leitura do arquivo JSON
with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo_json:
    dados_lidos = json.load(arquivo_json)

# Exibindo os dados na tela
print("\nDados lidos do arquivo JSON:")
print(f"Nome: {dados_lidos['Nome']}")
print(f"Idade: {dados_lidos['Idade']}")
print(f"Cidade: {dados_lidos['Cidade']}")