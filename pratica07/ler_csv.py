# Crie um script en Python que leia um arquivo CSV e exiba os dados na tela. O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.

import csv

# Nome do arquivo CSV
arquivo_csv = "dados_pessoais.csv"

try:
    with open(arquivo_csv, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        
        # Lê e exibe cada linha
        for linha in leitor:
            nome, idade, cidade = linha
            print(f"Nome: {nome} | Idade: {idade} | Cidade: {cidade}")

except FileNotFoundError:
    print(f"Erro: O arquivo '{dados_pessoais.csv}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
